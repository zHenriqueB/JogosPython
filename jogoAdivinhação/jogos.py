import adivinhacao
import forca


print("--------------------------------------------------------")
print("*************JOGOS**************")
print("--------------------------------------------------------")
print("Selecione o jogo que deseja jogar")
print("--------------------------------------------------------")



print("(1) Jogo de adivinhação")
print("(2) Jogo da forca")

jogo = input("Digite o número do jogo")

if (jogo ==1):
    
    print("Jogando adivinhação")
adivinhacao.jogar()

if (jogo ==2):
    
    print("Jogando forca")
forca.jogar()

