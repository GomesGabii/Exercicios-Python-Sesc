#22. Faça um algoritmo para ler três números e ordene-os em ordem crescente.
#Resposta:

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
    if numero2 <= numero3:
        medio = numero2
        maior = numero3
    else:
        medio = numero3
        maior = numero2
elif numero2 <= numero1 and numero2 <= numero3:
    menor = numero2
    if numero1 <= numero3:
        medio = numero1
        maior = numero3
    else:
        medio = numero3
        maior = numero1
else:
    menor = numero3
    if numero1 <= numero2:
        medio = numero1
        maior = numero2
    else:
        medio = numero2
        maior = numero1

print("Os números em ordem crescente são:", menor, medio, maior)
