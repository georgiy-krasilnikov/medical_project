import webbrowser

import PySimpleGUI as sg

from windows import start_window, enter_window, register_window, choice_window, class_window, load_window, download_window
from user import check_user, register_user
from classification import result
from images import load_images, download_images

while True:
    event, values = start_window.read()
    if event == 'https://oftal.ru/':
        webbrowser.open(event)
    elif event == 'click':
        event, values = enter_window.read()
        if event == 'enter':
            count = 0
            while check_user(values) == False and count < 5:
                sg.popup_ok('Ошибка', no_titlebar=True, auto_close_duration=2, auto_close=True)
                event, values = enter_window.read()
                count += 1
            if count >= 5:
                start_window.close()
                enter_window.close()
                event, values = register_window.read()
                if event == 'register':
                    register_user(values)
                    sg.popup('Вы зарегистрировались', no_titlebar=True, auto_close_duration=2, auto_close=True)
                    register_window.close()
            start_window.close()
            enter_window.close()
            event, values = choice_window.read()
            while event != sg.WIN_CLOSED:
                if event == 'variant1':
                    choice_window.close()
                    event, values = class_window.read()
                    while event != sg.WIN_CLOSED:
                        if event == 'class':
                            file_path = values['Выбрать']
                            zone = 'limb'
                            if values['perelimb'] == True:
                                zone = 'perelimb'
                                res = result(file_path, 'perelimb')
                            else:
                                res = result(file_path, 'limb')
                            load_images(file_path, zone, None, res)
                            event, values = class_window.read()
                elif event == 'variant2':
                    event, values = load_window.read()
                    while event != sg.WIN_CLOSED:
                        if event == 'load':
                            zone = 'limb'
                            sample = 'train'
                            info = 'bolen'
                        if values['limb'] == False:
                            zone = 'perelimb'
                        if values['train'] == False:
                            sample = 'test'
                        if values['bolen'] == False:
                            info = 'zdorov'
                        load_images(values['Выбрать'], zone, sample, info)
                        sg.popup('Загружено', no_titlebar=True, auto_close_duration=2, auto_close=True)
                        event, values = load_window.read()
                elif event == 'variant3':
                    event, values = download_window.read()
                    while event != sg.WIN_CLOSED:
                        if event == 'download':
                            download_images(limb=values['limb'], perelimb=values['perelimb'])
                            sg.popup('Выгружено', no_titlebar=True, auto_close_duration=2, auto_close=True)
                            event, values = download_window.read()
    elif event == sg.WIN_CLOSED:
        break


