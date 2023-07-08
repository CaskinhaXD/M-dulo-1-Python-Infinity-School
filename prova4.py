from random import *

def resp_Numero(numero):
    tentativas = int()
    while True:
        palpite = int(input("Qual o seu palpite de número? (0 a 50) "))
        
        if (palpite == numero):
            return print(f"O número {numero} foi acertado em {tentativas} tentativas")
        else:
            if (palpite > numero):
                print("O número é menor que o palpite.")
            else:
                print("O número é maior que o palpite.")
        
        tentativas += 1
        
numero = randint(0, 50)
resp_Numero(numero)