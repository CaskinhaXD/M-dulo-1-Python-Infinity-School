resposta = int(input("Digite um número inteiro: "))

calc = resposta % 2

if (calc != 1):
    # Resposta de máquina
    # print(f"Número ok: {calc} e {resposta}")
#else:
    resposta -= 1
    # Resposta de máquina
    # print(f"Número agora ok: {resposta}")
    
total = int()

while int(resposta >= 0):    
    total += resposta
    resposta -= 2

print(total)
