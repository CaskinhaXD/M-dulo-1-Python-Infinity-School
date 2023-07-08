soma = 0
somaPares = 0

for _ in range(6):
    num = int(input("Digite um número: "))
    
    soma += num
    
    if (num % 2 == 0):
        somaPares += num

print("Soma de todos os números:", soma)
print("Soma dos números pares:", somaPares)