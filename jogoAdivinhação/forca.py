def jogar():


    print("--------------------------------------------------------")
    print("------Bem vindo ao jogo da forca-----")
    print("--------------------------------------------------------")

    palavra_secreta = "banana".upper()
    letras_corretas = ["_","_","_","_","_","_"]
  
    enforcou = False
    acertou = False
    tentativas = 0
    
    print("A palavra é ? {}".format(letras_corretas))
    
    while(not enforcou and not acertou):
            resposta = input("Qual a letra ? ")
            resposta = resposta.strip().upper()
        
        
        
            if (resposta in palavra_secreta):
                index = 0
            
                for letra in palavra_secreta:
                    if(resposta.upper() == letra.upper()):
                            letras_corretas[index] = letra
                    index +=1    
                           
            else:
                    tentativas+=1
            enforcou = tentativas == 6
            acertou = "_" not in letras_corretas
            print(letras_corretas)
            
            
    if(acertou):
            print("VOCÊ GANHOU")    
            print("Fim do jogo ")    
    else:
        print("VOCÊ PERDEU")
        print("Fim do jogo ")   
                

if (__name__ == '__main__'):
    
    jogar() 