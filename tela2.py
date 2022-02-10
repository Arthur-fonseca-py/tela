import PySimpleGUI as sg

sg.theme('DarkAmber')   
#todas as coisas dentro da janela
layout = [  [sg.Text('Nome'), sg.InputText()],
            [sg.Text('Idade'), sg.InputText()],
            [sg.Button("enviar dados") ]
]
#criando a janela
window = sg.Window('Dados de Usuario', layout)
#guarda o valor recebido
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
    #se o usuário fechar a janela ou clicar em cancelar
        break
    
    print("sua idade é",values)
    #voltar o valor 

window.close()