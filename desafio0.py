# A ideia do projeto Desafio0, é criar algo para me ajudar no calculo dos 80 pontos da escola.

# Etapas:
# 1° Etapa e 2° Etapa:
# Pontuação: 30
# 3° Etapa:
# Pontuação: 40

def obter_etapa():
    while True:
        resposta = input("Em qual etapa você está? (1, 2, 3): ")
        if resposta in ['1', '2', '3']:
            return int(resposta)
        else:
            print("Resposta inválida. Por favor, escolha 1, 2 ou 3.")

def obter_provasEtapa(provas, provasNota):
    notas = []
    while True:
        rangeTot = provas
        for _ in range(rangeTot):
            resposta = input("Digite as suas notas dessa etapa (Ou 'q' para sair): ")
            if resposta.lower() == 'q':
                break
            try:
                nota = float(resposta)
                if sum(notas) + nota <= provasNota:
                    notas.append(nota)
                else:
                    print(f"Nota inválida. A soma das notas excede o limite da etapa que é {limite}.")
                    rangeTot = rangeTot + 1
            except ValueError:
                print("Valor inválido. Por favor, digite um número válido.")
        return notas

def obter_etapaPassada(limite):
    notas = []
    while True:
        resposta = input("Digite a nota da(s) etapa(s) passada(s) até agora (Ou 'q' para sair): ")
        if resposta.lower() == 'q':
            break
        try:
            nota = float(resposta)
            if sum(notas) + nota <= limite:
                notas.append(nota)
            else:
                print(f"Nota inválida. A soma das notas excede o limite da etapa que é {limite}.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")

    return notas

def obter_pontosEtapa(limite, notaEtapa):
    pontosEtapa = 0
    
    newLimite = limite - notaEtapa
    
    resposta = int(input(f"Quantos pontos ainda faltam para serem destribuidos na sua etapa? (Max: {newLimite}) "))
    
    if (resposta > newLimite):
        print(f"Nota inválida. Sua etapa vai ser considerada que ainda faltam 0 pontos a serem destribuidos")
    
        
    return pontosEtapa

etapaN = obter_etapa()
tot = 100

if (etapaN == 1):
    etapaS = "Primeira Etapa"
    limite = 0
    totDisp = tot - 30
elif (etapaN == 2):
    etapaS = "Segunda Etapa"
    limite = 30
    tot -= limite
else:
    etapaS = "Terceira Etapa"
    limite = 60
    tot -= limite

if (etapaN != 1):
    notaEtapaPassadaTot = obter_etapaPassada(limite)

print("Ok, foi selecionado que você está na", etapaS, "\nDe acordo com essa informação, você tem ainda", tot, "pontos para serem distribuidos.")

provas = int(input("Quantas provas ja aconteceram nessa etapa? (Max: 10) "))

#Terminar a partir daqui
if (provas != 0):
    provasNota = int(input("Quantos pontos essas provas valeram? "))

    notaEtapaSep = obter_provasEtapa(provas, provasNota)
    notaEtapaTot = sum(notaEtapaSep)

    if (etapaN == 1):
        totAnoSobrando = 100 - notaEtapaTot
        totAno = notaEtapaTot
    else:
        notaEtapaPassadaTotSoma = sum(notaEtapaPassadaTot)
        totAnoSobrando = 100 - (notaEtapaTot + notaEtapaPassadaTotSoma)
        totAno = notaEtapaTot + notaEtapaPassadaTotSoma

    print("Ok, sua nota da etapa foi", notaEtapaTot, "\nNo ano você ainda pode conseguir com os pontos que você tem", totAnoSobrando, "pontos\nVocê possui", totAno)

calcPorc = (totAnoSobrando + totAno)

pontosFalt = obter_pontosEtapa(limite, notaEtapaTot)

calcPorc += pontosFalt

if (calcPorc >= 80):
    print("Você ainda consegue tirar 80 pontos no ano, pois atualmente juntando seus pontos e os pontos que ainda faltam para serem destribuidos, você possui:", calcPorc)
else:
    print("Você não consegue tirar 80 pontos no ano, pois atualmente juntando seus pontos e os pontos que ainda faltam para serem destribuidos, você possui:", calcPorc)