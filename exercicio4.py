email = str(input("Digite o seu e-mail: "))
senha = str(input("Digite a sua senha: "))

branco = int()
canA = int()
canB = int()
nulo = int()
tot = int()

for _ in range(10):
    voto = int(input("Qual o seu voto? (0: Voto em Branco | 1: Candidato A | 2: Candidato B)"))
    
    if (voto == 0):
        branco += 1
    elif (voto == 1):
        canA += 1
    elif (voto == 2):
        canB += 1
    else:
        nulo += 1
    
    print("Seu voto foi computado!")
    tot += 1

confirmSenha = str(input("Qual a sua senha?: "))

if (senha == confirmSenha):
    print(f"O total de votos foi {tot}\nOs votos ao candidato A foram {canA}\nOs votos ao candidato B foram {canB}\nOs votos em branco foram {branco}\nOs votos nulos foram {nulo}")
else:
    print("Senha incorreta")