def jogar():


    print("--------------------------------------------------------")
    print("------Bem vindo ao jogo da forca-----")
    print("--------------------------------------------------------")

    palavra_secreta = "banana"
    letras_corretas = ["_","_","_","_","_","_"]
  
    enforcou = False
    acertou = False
    
    print("A palavra é ? {}".format(letras_corretas))
    
    while(not enforcou and not acertou):
        resposta = input("Qual a letra ? ")
        resposta = resposta.strip()
        print("jogando...")
        
        index = 0
        
        for letra in palavra_secreta:
            if(resposta.upper() == letra.upper()):
               letras_corretas[index] = letra
            index = index+1    
        print(letras_corretas)        


if (__name__ == '__main__'):
    
    jogar()