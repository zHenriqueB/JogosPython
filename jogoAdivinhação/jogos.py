import adivinhacao
import forca


print("--------------------------------------------------------")
print("*************JOGOS**************")
print("--------------------------------------------------------")
print("Selecione o jogo que deseja jogar")
print("--------------------------------------------------------")



print("(1) Jogo de adivinhação")
print("(2) Jogo da forca")

escolha = int(input("Digite o número do seu jogo !"))



if escolha == 1 :
    adivinhacao.jogar()
    
if escolha == 2 :
        forca.jogar()

