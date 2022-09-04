
from ast import Break
from bdb import Breakpoint


print("--------------------------------------------------------")
print("Bem vindo ao jogo de adivinhação")
print("--------------------------------------------------------")


numero_secreto = 42
total_de_tentativas = 3
rodada =1

for rodada in range(rodada,total_de_tentativas+1):
    print("Tentativa {} de {}".format(rodada,total_de_tentativas) )
    chute = input("Digite o seu numero entre 1 e 100:    ")
    
    if (int(chute)<1 or int(chute) >100 ):
        print("Você deve digitar um numero de 1 a 100 !")
        continue 
   
    acertou = numero_secreto == int(chute)
    maior=  int(chute) > numero_secreto
    menor=  int(chute) < numero_secreto
    
    if (acertou):
      print("Você acertou !")
      print("Fim do jogo !")
      break
    else:
        if (menor): 
            print("chutou um número mais baixo que o numero secreto")
            
        elif (maior): 
            print("chutou um número mais alto que o numero secreto ")
        
    if( rodada == 3):
         print("GAME OVER")
    
    
    