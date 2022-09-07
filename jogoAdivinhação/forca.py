def jogar():


    print("--------------------------------------------------------")
    print("------Bem vindo ao jogo da forca-----")
    print("--------------------------------------------------------")

    palavra_secreta = "banana"
  
    enforcou = False
    acertou = False
    
    while(not enforcou and not acertou):
        resposta = input("Qual é a palavra secreta?")
        resposta = resposta.strip()
        print("jogando...")
        
        index = 0
        
        for letra in palavra_secreta:
            if(resposta.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra,index))
            index = index+1    
                


if (__name__ == '__main__'):
    
    jogar()