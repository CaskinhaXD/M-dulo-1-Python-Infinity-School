cBene = 0
cSal = 0

for _ in range(5):
    salario = int(input("Qual o salário do cidadão? "))
    nFilhos = int(input("Quantos filhos o cidadão possui? "))
    
    if (nFilhos > 3):
        cSal += salario
    
    if (salario <= 1200):
        cBene += 1

print("Pessoas com beneficios:", cBene)
print("Soma salários com mais de 3 filhos:", cSal)