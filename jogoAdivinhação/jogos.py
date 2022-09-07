import adivinhacao
import forca

def escolhe_jogo():

    print("--------------------------------------------------------")
    print("*************JOGOS**************")
    print("--------------------------------------------------------")
    print("Selecione o jogo que deseja jogar")
    print("--------------------------------------------------------")



    print("(1) Jogo de adivinhação")
    print("(2) Jogo da forca")

    escolha = int(input("Digite o número do seu jogo !"))
    if escolha == 1 :
        print("Jogando adivinhação")
        adivinhacao.jogar()
    if escolha == 2 :
        print("Jogando forca")
        forca.jogar()
        
        
if(__name__ =='__main__'):        
    escolhe_jogo()
