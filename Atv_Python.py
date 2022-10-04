from imaplib import Time2Internaldate
import os
import PySimpleGUI as sg
import csv

jogador = []
posição = []
nota = []
Time = []
Time_Titular = []



def criar():
    i = 0
    jogador.clear()
    posição.clear()
    nota.clear()
    Time.clear()
    file = open("hexa.txt",'w')
    Elenco = ()
    for i in range(23):
        if (i < 3):
            layout = [
                [sg.Text('Digite o nome e a nota do goleiro')],
                [sg.Text('Nome: ', size=(10, 1)), sg.Input(key='nome')],
                [sg.Text('Nota: ', size=(10, 1)), sg.Input(key='nota')],
                [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
            ]

            janela = sg.Window('Bem -vindo a convocação da seleção brasileira', layout, element_justification='center')

            evento, dados = janela.read()
            nome = dados['nome']
            notas = dados['nota']
            jogador.insert(i,nome)
            nota.insert(i,int(notas))
            posição.insert(i, "Goleiro")
            janela.close()
            while nota[i] < 0 or nota[i] > 10:
                  print("Nota invalida, digite novamente")
                  nota.insert(i, int(input("Digite a nota do goleiro: ")))
        elif (i >= 3 and i < 7):
            layout = [
                [sg.Text('Digite o nome e a nota do lateral')],
                [sg.Text('Nome: ', size=(10, 1)), sg.Input(key='nome')],
                [sg.Text('Nota: ', size=(10, 1)), sg.Input(key='nota')],
                [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
            ]

            janela = sg.Window('Bem -vindo a convocação da seleção brasileira', layout, element_justification='center')

            evento, dados = janela.read()
            nome = dados['nome']
            notas = dados['nota']
            jogador.insert(i, nome)
            nota.insert(i, int(notas))
            posição.insert(i, "Lateral")
            janela.close()
            while nota[i] < 0 or nota[i] > 10:
                print("Nota invalida, digite novamente")
                nota.insert(i, int(input("Digite a nota do Lateral: ")))

        elif (i >= 7 and i < 11):
            layout = [
                [sg.Text('Digite o nome e a nota do zagueiro')],
                [sg.Text('Nome: ', size=(10, 1)), sg.Input(key='nome')],
                [sg.Text('Nota: ', size=(10, 1)), sg.Input(key='nota')],
                [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
            ]

            janela = sg.Window('Bem -vindo a convocação da seleção brasileira', layout, element_justification='center')

            evento, dados = janela.read()
            nome = dados['nome']
            notas = dados['nota']
            jogador.insert(i, nome)
            nota.insert(i, int(notas))
            posição.insert(i, "Lateral")
            janela.close()
            while nota[i] < 0 or nota[i] > 10:
                layout = [
                    [sg.Text('Digite a nota novamente')],
                    [sg.Text('Nota: ', size=(10, 1)), sg.Input(key='nota')],
                    [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
                ]

                janela = sg.Window('Nota invalida!', layout, element_justification='center')


                notas = dados['nota']
                jogador.insert(i, nome)
                nota.insert(i, int(notas))
                janela.close()
        elif (i >= 11 and i < 17):
            layout = [
                [sg.Text('Digite o nome e a nota do meio-campista')],
                [sg.Text('Nome: ', size=(10, 1)), sg.Input(key='nome')],
                [sg.Text('Nota: ', size=(10, 1)), sg.Input(key='nota')],
                [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
            ]

            janela = sg.Window('Bem -vindo a convocação da seleção brasileira', layout, element_justification='center')

            evento, dados = janela.read()
            nome = dados['nome']
            notas = dados['nota']
            jogador.insert(i, nome)
            nota.insert(i, int(notas))
            posição.insert(i, "Meio-Campista")
            janela.close()

            while nota[i] < 0 or nota[i] > 10:
                layout = [
                    [sg.Text('Digite a nota novamente')],
                    [sg.Text('Nota: ', size=(10, 1)), sg.Input(key='nota')],
                    [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
                ]

                janela = sg.Window('Nota invalida!', layout, element_justification='center')

                notas = dados['nota']
                jogador.insert(i, nome)
                nota.insert(i, int(notas))
                janela.close()
        elif (i >= 17 and i < 23):
            layout = [
                [sg.Text('Digite o nome e a nota do Atacante')],
                [sg.Text('Nome: ', size=(10, 1)), sg.Input(key='nome')],
                [sg.Text('Nota: ', size=(10, 1)), sg.Input(key='nota')],
                [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
            ]

            janela = sg.Window('Bem -vindo a convocação da seleção brasileira', layout, element_justification='center')

            evento, dados = janela.read()
            nome = dados['nome']
            notas = dados['nota']
            jogador.insert(i, nome)
            nota.insert(i, int(notas))
            posição.insert(i, "Atacante")
            janela.close()
            while nota[i] < 0 or nota[i] > 10:
                layout = [
                    [sg.Text('Digite a nota novamente')],
                    [sg.Text('Nota: ', size=(10, 1)), sg.Input(key='nota')],
                    [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
                ]

                janela = sg.Window('Nota invalida!', layout, element_justification='center')

                notas = dados['nota']
                jogador.insert(i, nome)
                nota.insert(i, int(notas))
                janela.close()

        Elenco = (jogador[i],posição[i],nota[i])
        file.write(str(Elenco)+"\n")
        Time.append(Elenco)
    file.close()
            
def Atualiza():
    layout = [
        [sg.Text('Digite o nome e a posição do jogador a ser atualizado')],
        [sg.Text('Nome: ', size=(10, 1)), sg.Input(key='nome')],
        [sg.Text('Posição: ', size=(10, 1)), sg.Input(key='posição')],
        [sg.Button('Entrar: ', button_color='green')],
    ]

    janela = sg.Window('Bem -vindo a convocação da seleção brasileira', layout, element_justification='center')

    evento, dados = janela.read()
    nome_Atualiza = dados['nome']
    posição_Atualiza = dados['posição']
    janela.close()
    file = open("hexa.txt",'r')
 
    
    i = 0
    for i in range(len(Time)):
        if nome_Atualiza == Time[i][0] and posição_Atualiza == Time[i][1]:
            del Time[i]
            layout = [
                [sg.Text('Digite a note do Atacante')],
                [sg.Text('Nome: ', size=(10, 1)), sg.Input(key='nome')],
                [sg.Text('Nota: ', size=(10, 1)), sg.Input(key='nota')],
                [sg.Text('Posição: ', size=(10, 1)), sg.Input(key='posição')],
                [sg.Button('Entrar: ', button_color='green'), sg.Button('Cancelar', button_color='red')],
            ]

            janela = sg.Window('Bem -vindo a convocação da seleção brasileira', layout, element_justification='center')

            evento, dados = janela.read()
            novo_nome = dados['nome']
            novo_notas = dados['nota']
            novo_posição = dados['posição']
            jogador.insert(i, novo_nome)
            nota.insert(i, int(novo_notas))
            posição.insert(i, novo_posição)
            janela.close()
            Elenco_Aux = (jogador[i],posição[i],nota[i])
            Time.append(Elenco_Aux)
            file.close()
            os.remove("hexa.txt")
            break

    fileWrite = open("hexa.txt",'w')
    for i in range(len(Time)):
        Elenco = (Time[i][0],Time[i][1],Time[i][2])
        fileWrite.write(str(Elenco)+"\n")
    
    fileWrite.close()

            
def Excluir():
    layout = [
        [sg.Text('Digite o nome e a posição do jogador a ser excluido')],
        [sg.Text('Nome: ', size=(10, 1)), sg.Input(key='nome')],
        [sg.Text('Posição: ', size=(10, 1)), sg.Input(key='posição')],
        [sg.Button('Entrar: ', button_color='green')],
    ]

    janela = sg.Window('Bem -vindo a convocação da seleção brasileira', layout, element_justification='center')

    evento, dados = janela.read()
    nome_excluir = dados['nome']
    posição_excluir = dados['posição']
    janela.close()
    i = 0
    file = open("hexa.txt",'r')

    for i in range(len(Time)):
        if nome_excluir == Time[i][0] and posição_excluir == Time[i][1]:
            del Time[i]
            file.close()
            os.remove("hexa.txt")
            break
        elif i == len(jogador):
            print("Dados não conferem")
        
    fileWrite = open("hexa.txt",'w')
    for i in range(len(Time)):
        Elenco = (Time[i][0],Time[i][1],Time[i][2])
        fileWrite.write(str(Elenco)+"\n")
    
    fileWrite.close()

def MontaTimeTitular():
    j = 0

    Goleiro_Notas = []
    for j in range(0, 3):
        Goleiro_Notas.append(Time[j][2])
    Goleiro_Notas.sort(reverse=True)

    Lateral_Notas = []
    for j in range(3, 7):
        Lateral_Notas.append(Time[j][2])
    Lateral_Notas.sort(reverse=True)

    Zagueiro_Notas = []
    for j in range(7, 11):
        Zagueiro_Notas.append(Time[j][2])
    Zagueiro_Notas.sort(reverse=True)

    Meia_Notas = []
    for j in range(11, 17):
        Meia_Notas.append(Time[j][2])
    Meia_Notas.sort(reverse=True)

    Atacantes_Notas = []
    for j in range(17, len(Time)):
        Atacantes_Notas.append(Time[j][2])
    Atacantes_Notas.sort(reverse=True)

    Time_Titular.clear()

    i=0
    for i in range(23):

        if (i < 3):
            while len(Time_Titular) < 1:
                if len(Time_Titular) < 3:
                    if Goleiro_Notas[0] == Time[i][2]:
                        Time_Titular.append(Time[i][0])
                    elif Lateral_Notas[1] == Time[i][2]:
                        Time_Titular.append(Time[i][0])

        elif (i >= 3 and i < 7):
            if len(Time_Titular) < 3:
                if Lateral_Notas[0] == Time[i][2]:
                    Time_Titular.append(Time[i][0])
                elif Lateral_Notas[1] == Time[i][2]:
                    Time_Titular.append(Time[i][0])

        if (i >= 7 and i < 11):
            if len(Time_Titular) < 5:
                if Zagueiro_Notas[0] == Time[i][2]:
                    Time_Titular.append(Time[i][0])
                elif Zagueiro_Notas[1] == Time[i][2]:
                    Time_Titular.append(Time[i][0])

        if (i >= 11 and i < 17):
            if len(Time_Titular) < 8:
                if Meia_Notas[0] == Time[i][2]:
                    Time_Titular.append(Time[i][0])
                elif Meia_Notas[1] == Time[i][2]:
                    Time_Titular.append(Time[i][0])
                elif Meia_Notas[2] == Time[i][2]:
                    Time_Titular.append(Time[i][0])

        if (i >= 17 and i < 24):
            if len(Time_Titular) < 11:
                if Atacantes_Notas[0] == Time[i][2]:
                    Time_Titular.append(Time[i][0])
                elif Atacantes_Notas[1] == Time[i][2]:
                    Time_Titular.append(Time[i][0])
                elif Atacantes_Notas[2] == Time[i][2]:
                    Time_Titular.append(Time[i][0])
    layout = [
        [sg.Listbox(values=Time_Titular, size=(30, 6), key='esc')],
        [sg.Button('OK')]
    ]
    janela = sg.Window('esc', layout)
    evento, dados = janela.read()
    janela.close()

def Lista_Convocados():
    layout = [
        [sg.Listbox(values=Time, size=(30, 6), key='esc')],
        [sg.Button('OK')]
    ]
    janela = sg.Window('esc', layout)
    evento, dados = janela.read()
    janela.close()


escolha = ''
while escolha != '6-sair':

    opções = ['1 - Fazer Convocação', '2 - Alterar jogador', '3 - Excluir jogador', '4 - Listar jogador', '5 - Time titular','6-sair']

    layout = [
        [sg.Listbox(values=opções, size=(30, 6), key='esc')],
        [sg.Button('OK')]
    ]
    janela = sg.Window('Menu principal', layout)
    evento, dados = janela.read()

    if len(dados) > 0:
        escolha = dados['esc'][0]
    janela.close()


    if escolha == '1 - Fazer Convocação':
          criar()

    if escolha == '2 - Alterar jogador':
          Atualiza()

    if escolha == '3 - Excluir jogador':
          Excluir()

    if escolha == '4 - Listar jogador':
        Lista_Convocados()

    if escolha == '5 - Time titular':
            MontaTimeTitular()

