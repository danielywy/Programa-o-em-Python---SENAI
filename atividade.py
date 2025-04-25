import numpy as np

array_2d = np.random.randint(0, 101, size=(5, 5))

media_linhas = np.mean(array_2d, axis=1)

valor_maximo = np.max(array_2d)
valor_minimo = np.min(array_2d)

print("Array 2D:")
print(array_2d)
print("\nMédia de cada linha:")
print(media_linhas)
print("\nValor máximo da matriz:", valor_maximo)
print("Valor mínimo da matriz:", valor_minimo)

vendas = np.array([120, 90, 150, 80, 200, 110, 50, 300])

vendas_maiores_que_100 = vendas[vendas > 100]

media_vendas = np.mean(vendas)
vendas_abaixo_da_media = np.sum(vendas < media_vendas)
vendas_normalizadas = vendas / np.max(vendas)


print("\nVendas maiores que 100:")
print(vendas_maiores_que_100)
print("\nQuantidade de vendas abaixo da média:", vendas_abaixo_da_media)
print("\nVendas normalizadas:")
print(vendas_normalizadas)
