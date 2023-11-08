import PySimpleGUI as sg

sg.theme('SystemDefault1')

font = ('Arial', 16)

layouts = [[
        [sg.Text('', font=font)],
        [sg.Image('images/logo.png', expand_x=True)],
        [sg.Text('', font=font)],
        [sg.Text('Интеллектуальная система распознавания', font=font)],
        [sg.Text('наличия патологии состояния',  font=font)],
        [sg.Text('микроциркуляции человека', font=font)],     
        [sg.Text('', font=font)],
        [sg.Button('Войти', size=(8, 2), key='click')],
        [sg.Text('', font=font)],
        [sg.Text('Перейти на сайт ЦТО', enable_events=True, key='https://oftal.ru/', font=('Arial', 12))]
    ],
    [
        [sg.Text('', font=font)],
        [sg.Image('images/logo.png', expand_x=True)],
        [sg.Text('', font=font)],
        [sg.Text('Введите логин:', font=('Arial', 12), key='login')],
        [sg.InputText('', size=(10, 2), key='login')],
        [sg.Text('Введите пароль:', font=('Arial', 12))],
        [sg.InputText('', size=(10, 2), key='password', password_char='*')],
        [sg.Button('Войти', size=(5, 1), key='enter', bind_return_key=True)],
        [sg.Text('', font=font)],
    ]]