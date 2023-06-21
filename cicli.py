lista = [1, 2, 3, 4]
print(lista)

# ciclo for sintassi

for i in lista:
    print(i)

lista1 = []
num = int(input("scrivi un numero"))
while num != 0:
    num = int(input("scrivi un numero"))
    lista1.append(num)


temp = 0
for j in lista1:
    print(j)
    temp += j

print("La somma di lista1 è" , temp)