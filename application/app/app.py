import webbrowser

import PySimpleGUI as sg

from user import check_user
from elements import layouts
from classification import result

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
            while check_user(values) == False:
                event, values = enter_window.read()
            window.close()
            enter_window.close()
            file_window = sg.Window('Интеллектуальная система ЦТО', layouts[2], element_justification='c', size=(500, 300))
            event, values = file_window.read()
            if event == 'class':
                file_path = values['Выбрать']
                if 'perelimb' in file_path:
                    result(file_path, 'perelimb')
                elif 'limb' in file_path:
                    result(file_path, 'limb')

    if event == sg.WIN_CLOSED:
        break


