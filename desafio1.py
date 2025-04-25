import statistics as stats

# Salários das empresas
empresa1 = [2500, 2800, 3000, 9500, 12000]
empresa2 = [5000, 5200, 5300, 5400, 5500]
empresa3 = [1000, 2000, 8000, 15000, 20000]
empresa4 = [3500, 4000, 4200, 4300, 6000]
empresa5 = [1200, 1500, 1800, 2500, 10000]

empresas = {
    'Empresa 1': empresa1,
    'Empresa 2': empresa2,
    'Empresa 3': empresa3,
    'Empresa 4': empresa4,
    'Empresa 5': empresa5
}

# Função para analisar os dados
def analisar_salarios(empresas):
    for nome, salarios in empresas.items():
        media = stats.mean(salarios)
        mediana = stats.median(salarios)
        try:
            moda = stats.mode(salarios)
        except stats.StatisticsError:
            moda = 'Sem moda'
        desvio = stats.stdev(salarios)

        print(f"\n📌 {nome}")
        print(f"Média: R${media:.2f}")
        print(f"Mediana: R${mediana:.2f}")
        print(f"Moda: {moda}")
        print(f"Desvio Padrão: R${desvio:.2f}")

# Executar análise
analisar_salarios(empresas)
