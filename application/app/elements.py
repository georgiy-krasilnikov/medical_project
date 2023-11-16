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
        [sg.Image('images/logo.png', expand_x=True)],
        [sg.Text('', font=font1)],
        [sg.Text('Введите логин:', font=font2)],
        [sg.InputText('', size=(10, 3), key='login')],
        [sg.Text('Введите пароль:', font=font2)],
        [sg.InputText('', size=(10, 3), key='password', password_char='*')],
        [sg.Button('Зарегистрироваться', size=(8, 1), key='register')],
        [sg.Text('', font=font1)],
    ],
    [
        [sg.Text('', font=font1)],
        [sg.Text('Выберите действие:', font=font2)],
        [sg.Text('', font=font1)],
        [sg.Button('Классифицировать изображение', size=(18, 3), key='variant1')],
        [sg.Text('', font=font1)],
        [sg.Button('Загрузить изображение в базу данных', size=(21, 3))],
        [sg.Text('', font=font1)],
    ],
    [
        [sg.Text('', font=font1)],
        [sg.Text('Загрузите выбранное изображение:', font=font2)],
        [sg.Text('', font=font1)],
        [sg.FilesBrowse(button_text='Выбрать', file_types=(('Изображения', '*.bmp'),))],
        [sg.Text('', font=font1)],
        [sg.Button('Классифицировать', size=(15, 2), key='class')],
        [sg.Text('', font=font1)],
    ],
    [
        [sg.Text('', font=font1)],
        [sg.Text('Загрузите выбранное изображение:', font=font2)],
        [sg.Text('', font=font1)],
        [sg.FilesBrowse(button_text='Выбрать', file_types=(('Изображения', '*.bmp'),))],
        [sg.Text('', font=font1)],
        [sg.Button('Загрузить', size=(12, 2), key='load')],
        [sg.Text('', font=font1)],
        [sg.Text('Выберите зону и выборку:', font=font2)],
        [sg.Radio('Зона лимб', 'zone', key='limb', font=font2)],
        [sg.Radio('Зона перелимб', 'zone', key='perelimb', font=font2)],
        [sg.Radio('Контрольная выборка', 'sample', key='test', font=font2)],
        [sg.Radio('Обучающая выборка', 'sample', key='train', font=font2)],
        [sg.Radio('Патология', 'info', key='bolen', font=font2)],
        [sg.Radio('Относительная норма', 'info', key='zdorov', font=font2)],
        [sg.Text('', font=font1)],
    ]
    ]