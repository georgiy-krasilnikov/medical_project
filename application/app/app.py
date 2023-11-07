import webbrowser

import PySimpleGUI as sg

font = ('Arial', 16)


sg.theme('SystemDefault1')

layout = [
        [sg.Text('', font=font)],
        [sg.Image('images/logo.png', expand_x=True)],
        [sg.Text('', font=font)],
        [sg.Text('Интеллектуальная система распознавания', font=font)],
        [sg.Text('наличия патологии состояния',  font=font)],
        [sg.Text('микроциркуляции человека', font=font)],     
        [sg.Text('', font=font)],
        [sg.Button('Войти', size=(8, 2))],
        [sg.Text('', font=font)],
        [sg.Text('Перейти на сайт ЦТО', enable_events=True, key='https://oftal.ru/', font=('Arial', 12))]
    ]

window = sg.Window('Интеллектуальная система ЦТО', layout, element_justification='c', size=(800, 500))

while True:
    event, values = window.read()
    if event.startswith("https://"):
        print(event)
        webbrowser.open(event)
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
