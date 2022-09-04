


print("----------------------------------------------------------")
print("Bem vindo ao jogo de adivinhação")
print("----------------------------------------------------------")


numero_secreto = 42

chute = input("Digite o seu numero :    ")

print("você digitou o numero", chute)


if (numero_secreto == int(chute)):
    print("acertou")

else:
    print("errou")
    print("Fim do jogo")
    
   