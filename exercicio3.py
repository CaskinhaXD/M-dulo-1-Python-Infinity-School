from random import *

def ganhou_perdeu(resposta):
    
    if (resposta == "ganhou"):
        return print("Você recebeu 1 vitória parabéns.")
    else:
        return print("Você perdeu.")

def loop(palp, ip):
    for _ in range(5):
        numero = randint(1, 2)
        
        calc = palp + numero
        
        corre = calc % 2
        
        tentativas += 1
        
        if ((corre == 0 and ip == "p") or (corre != 0 and ip == "i")):
            vitorias += 1
            ganhou_perdeu("ganhou")
        else:
            ganhou_perdeu("perdeu")

def resp_Numero():
    tentativas = int()
    vitorias = int()
    
    palp = int(input("Qual o seu palpite de número? "))
    ip = str(input("O número é impar ou par? (i ou p)"))
    
    loop(palp, ip)
            
    return print(f"Você teve {vitorias} vitórias.")


resp_Numero()