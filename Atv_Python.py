from imaplib import Time2Internaldate


jogador = []
posição = []
nota = []
Elenco = ()
Time =[]

def criar():
    i = 0
    for i in range(3):
        if i == 0:
            jogador.insert(i,"Alisson")
            posição.insert(i,"Goleiro")
            nota.insert(i,8)
            
        elif i == 1:
            jogador.insert(i,"Paquetá")
            posição.insert(i,"Meio-campista")
            nota.insert(i,9)
            
        elif i == 2:
            jogador.insert(i,"Neymar")
            posição.insert(i,"Atacante")
            nota.insert(i,10)
        Elenco = (jogador[i],posição[i],nota[i])
        Time.append(Elenco)
            
def Atualiza():
    Nome_Atualizar = input("Digite o nome a ser alterado: ")
    Posicao_Atualizar = input("Digite a posição do jogador a ser alterado: ")
    
    i = 0
    for i in range(len(Time)):
        if Nome_Atualizar == Time[i][0] and Posicao_Atualizar == Time[i][1]:
            del Time[i]
            
            jogador.insert(i,"Antony")
            posição.insert(i,"Goleiro")
            nota.insert(i,"7")
            Elenco_Aux = (jogador[i],posição[i],nota[i])
            Time.append(Elenco_Aux)
            
            
            break
  
            
def Excluir():
    Nome_Excluir= input("Digite o nome a ser alterado: ")
    Posicao_Excluir = input("Digite a posição do jogador a ser alterado: ")
    
    i = 0
    for i in range(len(jogador)):
        if Nome_Excluir == Time[i][0] and Posicao_Excluir == Time[i][1]:
            del Time[i]
            break
        elif i == len(jogador):
            print("Dados não conferem") 
                
            
criar()
Atualiza()
print(Time)