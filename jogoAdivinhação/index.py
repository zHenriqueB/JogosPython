
print("----------------------------------------------------------")
print("Bem vindo ao jogo de adivinhação")
print("----------------------------------------------------------")


numero_secreto = 42

chute = input("Digite o seu numero :    ")

print("você digitou o numero", chute)
acertou = numero_secreto == int(chute)
maior=  int(chute) > numero_secreto
menor=  int(chute) < numero_secreto


if (acertou):
    print("Você acertou")

else:
    if (menor): 
        print("chutou um numero mais baixo que o numero secreto")
        print("errou")
        print("Game Over")
    elif (maior): 
        print("chutou um numero mais alto que o numero secreto ")
        print("errou")
        print("Game Over")
    
    
    
   