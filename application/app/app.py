import webbrowser

import PySimpleGUI as sg

from user import check_user, register_user
from elements import layouts
from classification import result
from images import load_images

sg.theme('SystemDefault1')

window = sg.Window('Интеллектуальная система ЦТО', layouts[0], element_justification='c', size=(800, 500))

while True:
    event, values = window.read()
    if event.startswith('https://'):
        webbrowser.open(event)
    if event == 'click':
        enter_window = sg.Window('Вход в систему', layouts[1], element_justification='c', size=(400, 350))
        event, values = enter_window.read()
        if event == 'enter':
            count = 0
            while check_user(values) == False and count < 5:
                sg.popup_ok('Ошибка')
                event, values = enter_window.read()
                count += 1

            if count >= 5:
                window.close()
                enter_window.close()
                register_window = sg.Window('Регистрация', layouts[2], element_justification='c', size=(400, 350))
                event, values = register_window.read()
                if event == 'register':
                    register_user(values)
                    register_window.close()
                
            window.close()
            enter_window.close()
            choice_window = sg.Window('Интеллектуальная система ЦТО', layouts[3], element_justification='c', size=(500, 350))
            event, values = choice_window.read()
            if event == 'variant1':
                choice_window.close()
                class_window = sg.Window('Интеллектуальная система ЦТО', layouts[4], element_justification='c', size=(500, 300))
                event, values = class_window.read()
                if event == 'class':
                    file_path = values['Выбрать']
                    if 'perelimb' in file_path:
                        result(file_path, 'perelimb')
                    elif 'limb' in file_path:
                        result(file_path, 'limb')
            else:
                choice_window.close()
                load_window = sg.Window('Интеллектуальная система ЦТО', layouts[5], element_justification='c', size=(800, 600))
                event, values = load_window.read()
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
                    sg.popup_ok('Загружено')
            
    if event == sg.WIN_CLOSED:
        break


