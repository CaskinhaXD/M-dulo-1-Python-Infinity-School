valor = float(input("Qual o valor do veículo? "))
sal = float(input("Qual o seu salário? "))
pag = float(input("Qual o período para pagamento em meses? "))

prest = valor / pag

print("O valor das prestações será de ", prest)

aceit = (sal * 30)/100

if (aceit > prest):
    print("Empréstimo aprovado.")
else:
    print("Empréstimo reprovado.")
    dif = prest - aceit
    print("Você precisa de um salário maior em", dif, "reais")