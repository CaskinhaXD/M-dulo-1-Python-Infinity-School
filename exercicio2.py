resposta = int(input("Digite um número inteiro: "))

calc = resposta % 2

if (calc != 0):
    # Resposta de máquina
    # print(f"Número ok: {calc} e {resposta}")
#else:
    resposta -= 1
    # Resposta de máquina
    # print(f"Número agora ok: {resposta}")
    
while int(resposta >= 0):
    print(resposta)
    
    resposta -= 2