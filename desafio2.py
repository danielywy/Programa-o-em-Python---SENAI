import statistics as stats

# ===== Módulo de Estatísticas =====

def calcular_media(notas):
    return stats.mean(notas)

def calcular_mediana(notas):
    return stats.median(notas)

def calcular_moda(notas):
    try:
        return stats.mode(notas)
    except stats.StatisticsError:
        return "Sem moda"

def calcular_desvio_padrao(notas):
    return stats.stdev(notas)

def calcular_amplitude(notas):
    return max(notas) - min(notas)

def menor_nota(notas):
    return min(notas)

def maior_nota(notas):
    return max(notas)


# ===== Módulo de Gestão de Alunos =====

def exibir_estatisticas(nome_aluno, notas):
    print(f"\n📊 Estatísticas para {nome_aluno}:")
    print(f"Notas: {notas}")
    print(f"Média: {calcular_media(notas):.2f}")
    print(f"Mediana: {calcular_mediana(notas):.2f}")
    print(f"Moda: {calcular_moda(notas)}")
    print(f"Desvio Padrão: {calcular_desvio_padrao(notas):.2f}")
    print(f"Amplitude: {calcular_amplitude(notas)}")
    print(f"Menor Nota: {menor_nota(notas)}")
    print(f"Maior Nota: {maior_nota(notas)}")

def processar_alunos(dados_alunos):
    for aluno, notas in dados_alunos.items():
        exibir_estatisticas(aluno, notas)


# ===== Execução Principal =====

alunos = {
    "Alice": [8.5, 7.0, 9.0, 8.5],
    "Bruno": [5.0, 6.0, 5.5, 6.5],
    "Carla": [10.0, 9.5, 9.0, 10.0],
    "Daniel": [3.5, 4.0, 3.0, 4.5],
    "Eduarda": [7.5, 8.0, 7.0, 8.0]
}

if __name__ == "__main__":
    processar_alunos(alunos)
