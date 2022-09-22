from imaplib import Time2Internaldate
import os
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
            jogador.insert(i, input("Digite o nome do goleiro: "))
            posição.insert(i, "Goleiro")
            nota.insert(i, int(input("Digite a nota: ")))
            while nota[i] < 0 or nota[i] > 10:

                  print("Nota invalida, digite novamente")
                  nota.insert(i, int(input("Digite a nota do goleiro: ")))
        elif (i >= 3 and i < 7):
            jogador.insert(i, input("Digite o nome do lateral: "))
            posição.insert(i, "Lateral")
            nota.insert(i, int(input("Digite a nota: ")))
            while nota[i] < 0 or nota[i] > 10:
                print("Nota invalida, digite novamente")
                nota.insert(i, int(input("Digite a nota: ")))
        elif (i >= 7 and i < 11):
            jogador.insert(i, input("Digite o nome do Zagueiro: "))
            posição.insert(i, "Zagueiro")
            nota.insert(i, int(input("Digite a nota: ")))
            while nota[i] < 0 or nota[i] > 10:
                print("Nota invalida, digite novamente")
                nota.insert(i, int(input("Digite a nota do Zagueiro: ")))
        elif (i >= 11 and i < 17):
            jogador.insert(i,input("Digite o nome do Meio_Campista: "))
            posição.insert(i, "Meio-campista")
            nota.insert(i, int(input("Digite a nota: ")))
            while nota[i] < 0 or nota[i] > 10:
                print("Nota invalida, digite novamente")
                nota.insert(i, int(input("Digite a nota do meia: ")))
        elif (i >= 17 and i < 23):
            jogador.insert(i,input("Digite o nome do Atacante: "))
            posição.insert(i, "Atacante")
            nota.insert(i, int(input("Digite a nota: ")))
            while nota[i] < 0 or nota[i] > 10:
                print("Nota invalida, digite novamente")
                nota.insert(i, int(input("Digite a nota do atacante: ")))
        Elenco = (jogador[i],posição[i],nota[i])
        file.write(str(Elenco)+"\n")
        Time.append(Elenco)
    file.close()
            
def Atualiza():
    Nome_Atualizar = input("Digite o nome a ser alterado: ")
    Posicao_Atualizar = input("Digite a posição do jogador a ser alterado: ")


    i = 0
    for i in range(len(jogador)):
        if Nome_Atualizar == Time[i][0] and Posicao_Atualizar == Time[i][1]:
            del Time[i]
            jogador.insert(i,input("Nome Do novo Jogador; "))
            posição.insert(i,input("Posição do novo Jogador: "))
            nota.insert(i,int(input("Nota do novo jogador: ")))
            Elenco_Aux = (jogador[i],posição[i],nota[i])
            Time.append(Elenco_Aux)
            os.remove("hexa.txt")
            break

    fileWrite = open("hexa.txt",'w')
    for i in range(len(Time)):
        Elenco = (Time[i][0],Time[i][1],Time[i][2])
        fileWrite.write(str(Elenco)+"\n")
    
    fileWrite.close()

            
def Excluir():
    Nome_Excluir = input("Digite o nome a ser Excluido: ")
    Posicao_Excluir = input("Digite a posição do jogador a ser excluido: ")
    
    i = 0
    for i in range(len(jogador)):
        if Nome_Excluir == Time[i][0] and Posicao_Excluir == Time[i][1]:
            del Time[i]
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

        if (i >= 17 and i < 23):
            if len(Time_Titular) < 11:
                if Atacantes_Notas[0] == Time[i][2]:
                    Time_Titular.append(Time[i][0])
                elif Atacantes_Notas[1] == Time[i][2]:
                    Time_Titular.append(Time[i][0])
                elif Atacantes_Notas[2] == Time[i][2]:
                    Time_Titular.append(Time[i][0])
    """ fileCSV = open("hexa.csv",'w')                
    writer = csv.writer(fileCSV)
    writer.writerows(Time_Titular)"""


def Lista_Convocados():
    i = 0
    for i in range(len(Time)):
        print(Time[i][0]+ " " +Time[i][1])


op = 0

while op != 6:
    print("1 - Fazer a convocação")
    print("2 - Aterar Jogador")
    print("3 - Excluir jogador")
    print("4 - Exibir Jogadores Convocados")
    print("5 - Exibir time Titular")
    print("6 - Sair")
    op = int(input("Escolha uma opção: "))

    if op == 1:
        criar()
        
    if op == 2:
            Atualiza()



    if op == 3:
            Excluir()



    if op == 4:
        Lista_Convocados()



    if op == 5:
            MontaTimeTitular()
