from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, Push, theme
)

theme('Material1')

layout_esquerda = [
    [Image(filename='cisco-logo.png')],
]

layout_direita = [
    [Text('Login:'), Input()],
    [Text('Senha:'), Input(password_char='*')],
    [Push(), Button('Login!')],
]

layout = [
    [Column(layout_esquerda), VSeparator(), Column(layout_direita)]
]

window = Window(
    'Tela de Login dos ASR Cisco',
    layout=layout,
)

while True:
    event, values = window.read()
    print(event, values)

window.close()