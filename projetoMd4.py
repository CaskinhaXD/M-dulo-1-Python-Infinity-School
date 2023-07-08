# Definir uma senha de 6 casas
def calc_casas(senha):
    casas = 1
    while True:
            calc = senha / 10
        
            if (calc > 1):
                casas += 1
                senha = calc
            else:
                break
    return casas
    

def obter_senha():
    while True:
        senha = int(input("Escreva uma senha com 6 casas: "))
        
        if (calc_casas(senha) == 6):
            print("Senha Ok")
            break
        elif(calc_casas(senha) >= 6):
            print("Sua senha possui mais que 6 casas.")
        else:
            print("Sua senha não possui 6 casas.")
    
    return senha

def confimar_senha(senhaPrConfirmar):
    while True:
        senhaConfirm = int(input("Digite a senha de confirmação: "))
        
        if (calc_casas(senhaConfirm) == 6):
            if (senhaConfirm == senhaPrConfirmar):
                print("As senhas batem.")
                break
            else:
                print("As senhas são diferentes.")
        elif(calc_casas(senhaConfirm) >= 6):
            print("Sua senha possui mais que 6 casas.")
        else:
            print("Sua senha não possui 6 casas.")
    
    return senhaConfirm

print("Coloque 3 senhas ao banco de dados de seu celular")

senhasBanco = []

count = 0
for _ in range(3):
    senhaPrConfirmar = obter_senha()

    senha = confimar_senha(senhaPrConfirmar)
    
    senhasBanco.insert(count, senha)
    count += 1
    
print("Seu banco de senhas:", senhasBanco)