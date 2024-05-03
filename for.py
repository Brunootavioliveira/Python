'''vogais = 0
nome = 'danilo'
for char in nome:
    if char == 'a' or


for i in range (10):
    print(i)

for i in range (1,10,2):#start,end,step
    print(i)

for i in range (10,1,-2):#start,end,step
    print(i)

senha_cad = "1234"
for i in range(3):
    senha = input("Diga sua senha: ")
    if senha == senha_cad:
        print("Acesso liberado")
        break
    print(f"Você é hacker? {2-i} tentativas restantes")
if senha != senha_cad:
    print("sai hacker")

for i in range(10):
    print(i,end = ' ')
    i = 1
    print(i)

soma = 0
for i in range(1,101):
    soma += i
print(soma)

lista = [1,True,'eofhwhfald',[23, 24],2.1]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3][0])
print(lista[4])
print(lista[5])#n existe


lista = []
print(lista)
lista.append(34)
print(lista)
lista.append(56)
print(lista)
lista.append(68)
print(lista)
'''

#ex1
'''lista = ['joao','lucas','patricia','danilo','gabriel']
for i in range(len(lista)):
    if lista[i] == 'danilo':
        print(f'Danilo foi encontrado na posição {i}')
        break
    else:
        print('Danilo não foi encontrado')'''

#ex2
'''materia = ['design','front','story','python','webDev']
prof = ['joao','lucas','patricia','danilo','caio']
for i in range(len(prof)):
    print(f'O professor {prof[i]} da aula de {materia[i]}')'''

#3

num = []
for i in range(10):
    numero = int(input('Digite os números:'))
    num.append(numero)
print('Lista dos numeros', num)

