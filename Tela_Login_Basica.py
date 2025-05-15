import PySimpleGUI as sg

layout = [[sg.Text("Usuário"), sg.Input(key="usuario", size=(20,1))], #Puxa tipo texto e um input
        [sg.Text("Senha"), sg.Input(key="senha", password_char="*", size=(20,1))], #passwrd_char="*" deixa senha oculta
        [sg.Checkbox("Salvar Login?")],
        [sg.Button("Entrar")]]

janela = sg.Window("Tela de Login", layout) #cria a janela Tela de Login e chama a variavel Layout

while True: #loop na interface, não para de funcinar
    eventos, valores = janela.read() #janela.red() para ler a janela
    if eventos == sg.WINDOW_CLOSED : #caso feche a janela o sistema pare de rodar
        break
    if eventos == "Entrar": #caso apertar em Entrar
        if valores["usuario"] == "Luiz" and valores["senha"] == "123456": #confere os valores
            print("Bem vindo")