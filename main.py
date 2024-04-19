#3
'''a = 80
b = 200
anos = 0
while a < b:
    a *= 1.03
    b *= 1.015
    anos += 1
print(anos)'''

#4
'''soma = 0
tent = 0
while tent < 5:
    num = input('Diga um número: ')
    while not num.isnumeric():
        print("Deve ser número!")
        num = input("Diga um número: ")
    num = int(num)
    soma += num
    tent += 1
print(f'A soma dos números foi {soma} e a média foi {soma/tent}')'''

#5
'''a = int(input("Diga um número: "))
b = int(input("Diga um número: "))
if a > b:
    aux = a
    a = b
    b =aux
while a <= b:
    print(a)
    a+=1'''

#6
'''usuario = input('Diga seu nome de usuario: ')
senha = input('Diga sua senha: ')
while True:
    usuario = input("Diga seu nome de usuario: ")
    senha = input'''

#7
'''i = 1
num = input('Diga um número para fazer a tabuada: ')
while not num.isnumeric():
    print("Deve ser número!")
    num = input('Diga um número para fazer a tabuada: ')
num = int(num)
if num >= 11:
    print('Deve ser menor que 10')
    num = input('Diga um número para fazer a tabuada: ')
while i <= 10:
    print(f"{num}*{i}={num*i}")
    i += 1'''


'''num = 1
i = 1
while num<= 10:
    print(f"Tabuada do {num}:")
    i = 1
    while i <= 10:
        print(f"{num}*{i} = {num*i}")
        i += 1
    num += 1 
    print()'''

'''num = 5
fatorial = num
fatorial_string = f"{num}! = {num}"
while num > 1:
    num-= 1
    fatorial *= num
    fatorial_string += f"*{num}"
fatorial_string += f" = {fatorial}"
print(fatorial_string)'''


#8
'''num = 15
i = 2 
while i < num**0.5:
    if num % i == 0: 
        print("Não é primo")
        break
    i+=1
if i >= num**0.5:
    print("É primo")'''

#13
'''salario = 1000
taxa = 0.015
partida = 1995
while partida < 2024:
    salario *= 1 + taxa
    taxa *= 2
    partida += 1
print(salario)'''

#14
'''primeiro = 0
segundo = 0
terceiro = 0
quarto = 0
while True
    num = input("Diga um número entre 0 e 100 e maior que 100 para sair:\n->")
    while not num.isnumeric():
        num = input("Diga um número entre 0 e 100 e maior que 100 para sair:\n->")
        if num<=25:
            primeiro += 1
        elif num <= 50:
            segundo += 1 
        elif num <= 75:
            segundo += 1
        elif num <= 100:
            segundo += 1   
        else:
            break'''

