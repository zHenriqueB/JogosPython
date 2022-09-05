import random


print("--------------------------------------------------------")
print("Bem vindo ao jogo de adivinhação")
print("--------------------------------------------------------")


numero_secreto = random.randrange(1,101,1)
total_de_tentativas = 0
rodada =1

print("Escolha seu nível de dificuldade ")
print("(1) Fácil   (2)  Médio   (3) Difícil")

nivel = int (input("Escolha seu nivel de dificuldade :"))

if (nivel ==1):
     total_de_tentativas=10
     print("Você escolheu o nivel de jogo fácil",   "você tem",total_de_tentativas,"tentativas")

if(nivel==2):
    total_de_tentativas=5
    print("Você escolheu o nivel de jogo médio",   "você tem",total_de_tentativas,"tentativas")
    
    if(nivel==3):
        total_de_tentativas=3
        print("Você escolheu o nivel de jogo difícil",   "você tem",total_de_tentativas,"tentativas")
        

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
    
    
    