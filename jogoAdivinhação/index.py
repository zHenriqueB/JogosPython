
print("--------------------------------------------------------")
print("Bem vindo ao jogo de adivinhação")
print("--------------------------------------------------------")


numero_secreto = 42
total_de_tentativas = 3
rodada =1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada,total_de_tentativas) )
    chute = input("Digite o seu numero :    ")
   
    acertou = numero_secreto == int(chute)
    maior=  int(chute) > numero_secreto
    menor=  int(chute) < numero_secreto
    
    if (acertou):
        print("Você acertou")
    else:
        if (menor): 
            print("chutou um número mais baixo que o numero secreto")
            
        elif (maior): 
            print("chutou um número mais alto que o numero secreto ")
        
    if( rodada == 3):
         print("GAME OVER")
    rodada = rodada + 1
    
    