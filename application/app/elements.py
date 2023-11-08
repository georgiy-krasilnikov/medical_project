import PySimpleGUI as sg

sg.theme('SystemDefault1')

font1 = ('Arial', 16)
font2 = ('Arial', 12)

layouts = [[
        [sg.Text('', font=font1)],
        [sg.Image('images/logo.png', expand_x=True)],
        [sg.Text('', font=font1)],
        [sg.Text('Интеллектуальная система распознавания', font=font1)],
        [sg.Text('наличия патологии состояния',  font=font1)],
        [sg.Text('микроциркуляции человека', font=font1)],     
        [sg.Text('', font=font1)],
        [sg.Button('Войти', size=(8, 2), key='click')],
        [sg.Text('', font=font1)],
        [sg.Text('Перейти на сайт ЦТО', enable_events=True, key='https://oftal.ru/', font=font2)]
    ],
    [
        [sg.Text('', font=font1)],
        [sg.Image('images/logo.png', expand_x=True)],
        [sg.Text('', font=font1)],
        [sg.Text('Введите логин:', font=font2)],
        [sg.InputText('', size=(10, 3), key='login')],
        [sg.Text('Введите пароль:', font=font2)],
        [sg.InputText('', size=(10, 3), key='password', password_char='*')],
        [sg.Button('Войти', size=(5, 1), key='enter')],
        [sg.Text('', font=font1)],
    ],
    [
        [sg.Text('', font=font1)],
        [sg.Text('Загрузите выбранное изображение:', font=font2)],
        [sg.Text('', font=font1)],
        [sg.FilesBrowse(button_text='Выбрать', file_types=(('Изображения', '*.bmp'),))],
        [sg.Text('', font=font1)],
        [sg.Button('Классифицировать', size=(15, 2), key='class')],
    ]]