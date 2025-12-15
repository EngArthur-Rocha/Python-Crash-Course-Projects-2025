milhao=[]
for value in range (1,1000001):
    milhao.append(value)
min(milhao)
max(milhao)
sum(milhao)

#Somando um milhão
milhao=[]
for value in range (1,1000001):
    milhao.append(value)
print(min(milhao))
print(max(milhao))
print(sum(milhao))

#Números ípares
impares=[]
for values in range (1,21,2):
    impares.append(values)
print(impares)

#Cubos
cubos=[]
for values in range (1,11):
    cubos.append(values**3)
print(cubos)

#Usando List Comprehension
cubos=[values**3 for values in range (1,11)]
print(cubos)