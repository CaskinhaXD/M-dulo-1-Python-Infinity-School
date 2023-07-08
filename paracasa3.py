valorTotal = float()
nomesTotal = str()

for _ in range(6):
    nomesTotal += str(input("Qual o nome do item comprado? ") + " ")
    valorTotal += float(input("Qual o valor do produto que foi comprado? "))

pagamento = str(input("Qual sera o tipo de pagamento? (Deb/Cred/Din) "))

if (pagamento == "Din" or pagamento == "Deb"):
    print("Valor do desconto: 7%")
    calc = (valorTotal * 7) / 100
    print(f"Valor da compra: {calc}")
else:
    parc = int(input("Qual vai ser o número de parcelas? "))
    if (parc == 1):
        print("Valor do desconto: 7%")
        calc = (valorTotal * 7) / 100
        print(f"Valor da compra: {calc}")
    elif (parc == 2):
        print("Valor do desconto: 3%")
        calc = (valorTotal * 3) / 100
        print(f"Valor da compra: {calc}")
    else:
        print(f"Valor da compra: {valorTotal}")
