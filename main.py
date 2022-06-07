from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, Push
)



layout_esquerda = [
    [Image(filename='cisco-logo.png')],
]

layout_direita = [
    [Text('E-mail:'), Input()],
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

print(window.read())

window.close()