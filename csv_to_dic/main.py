import csv

with open('clientes.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=';')
    clientes = [row for row in reader]


def calcular_media_idades():
    soma = 0
    for item in clientes:
        soma += int(item["idade"])

    media = soma / len(clientes)
    return media

def calcular_media_renda():
    soma = 0
    for item in clientes:
        soma += int(item["salario"])

    media = soma / len(clientes)
    return media

print('Media das idades:',calcular_media_idades())
print('Media das rendas:',calcular_media_renda())      
