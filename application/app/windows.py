import PySimpleGUI as sg

from elements import layouts 

start_window = sg.Window('Интеллектуальная система ЦТО', layouts[0], element_justification='c', size=(800, 500))
enter_window = sg.Window('Вход в систему', layouts[1], element_justification='c', size=(400, 350))
register_window = sg.Window('Регистрация', layouts[2], element_justification='c', size=(400, 350))
choice_window = sg.Window('Интеллектуальная система ЦТО', layouts[3], element_justification='c', size=(600, 450))
class_window = sg.Window('Интеллектуальная система ЦТО', layouts[4], element_justification='c', size=(500, 300))
load_window = sg.Window('Интеллектуальная система ЦТО', layouts[5], element_justification='c', size=(800, 600))
download_window = sg.Window('Интеллектуальная система ЦТО', layouts[6], element_justification='c', size=(550, 300))