ano = int(input("Informe seu ano de nascimento: "))

form = 2023 - ano

if (form < 18):
    print("Inapto para o serviço militar!")
    dif = 18 - form
    print("Para estar apto você precisa ter 18 anos, ainda faltam", dif, "anos.")
else:
    print("Apto para o serviço militar!")