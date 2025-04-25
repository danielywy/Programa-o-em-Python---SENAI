import statistics
import matplotlib.pyplot as plt

def moda1(lista):
    moda = statistics.mode(lista)
    print('Moda: ', moda)

def mediana1(lista):
    mediana = statistics.median(lista)
    print('Mediana: ', mediana)

def varianca1(lista):
    varianca = statistics.variance(lista)
    print('Variância: ', varianca)

def desvio1(lista):
    desvio = statistics.stdev(lista)
    print(f'Desvio padrão: {desvio:.2f}')

def media1(lista):
    media = statistics.mean(lista)
    print('Média: ', media)

empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]

def handle(lista, nome):
    print(f'EMPRESA {nome}')
    print('----------------------------')
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)

# Chamadas
handle(empresa1, '1')
handle(empresa2, '2')
handle(empresa3, '3')
handle(empresa4, '4')

# Plot gráfico de barras
empresas = ['Empresa 1', 'Empresa 2', 'Empresa 3', 'Empresa 4']
medias = [
    statistics.mean(empresa1),
    statistics.mean(empresa2),
    statistics.mean(empresa3),
    statistics.mean(empresa4)
]

plt.figure()
plt.bar(empresas, medias, color='purple')
plt.title('Média Salarial por Empresa')
plt.ylabel('Salário Médio')
plt.xlabel('Empresa')
plt.show()
