# Registrar nome e telefone cliente e registrar em uma lista, que ficara executando
# Sortear um cliente ao receber fim
from random import *

clientes = []
celulares = []
total = int()

while True:
    nome = str(input("Qual o nome do cliente? "))
    
    if nome == "fim":
        numero = randint(0, total)
        numero0 = int(numero)
        
        sorteadoNome = clientes[int(numero0)]
        sorteadoNumero = celulares[int(numero0)]
        
        print(f"O cliente sorteado foi {sorteadoNome} e seu número de telefone é {sorteadoNumero}")
        
        break
    else:
        telefone = int(input("Qual o número do cliente? "))
        
        clientes.append(nome)
        celulares.append(telefone)
        total += 1