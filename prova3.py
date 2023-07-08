menos20 = 0
mais40 = 0
sexoMaisNova = str("")
maisVelho = str("")

idadeMaior = 0
idadeMenor = 100000000

for _ in range(5):
    nome = str(input("Qual o nome do primeiro integrante do grupo? "))
    idade = int(input("Qual a idade de " + nome + "? "))
    sexo = str(input("Qual o sexo de " + nome + "? (H/M) "))
    
    if (idade < 20):
        menos20 = menos20 + 1
        
    if (idade > 40):
        mais40 = mais40 + 1
        
    if (idadeMaior < idade):
        idadeMaior = idade
        maisVelho = nome
        
    if (idadeMenor > idade):
        idadeMenor = idade
        sexoMaisNova = sexo

        
print("Pessoa mais velha:", maisVelho)
print("Pessoas com menos de 20 anos:", menos20)
print("Pessoas com mais de 40 anos:", mais40)
print("Sexo da pessoa mais nova:", sexoMaisNova)