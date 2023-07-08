num0 = float(input("Qual foi a primeira nota? "))
num1 = float(input("Qual foi a segunda nota? "))
num2 = float(input("Qual foi a terceira nota? "))
num3 = float(input("Qual foi a quarta nota? "))

print("As notas dadas foram: ", num0, num1, num2, num3)

calc = (num0 + num1 + num2 + num3)/4

if (calc > 7):
    print("O aluno está aprovado.")
elif (5 < calc <= 7):
    print("O aluno está de recuperação.")
else:
    print("O aluno está reprovado.")

print("A média foi: ", calc)