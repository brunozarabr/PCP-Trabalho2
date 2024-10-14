import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carrega os dados do arquivo CSV
data = pd.read_csv("resultado.csv")

# Remove espaços em branco dos nomes das colunas
data.columns = data.columns.str.strip()

# Obtém os valores únicos de intervalo_x e intervalo_y
intervalo_x_values = data['intervalo_x'].unique()
numero_threads_values = data['numero_threads'].unique()
intervalo_y_values = data['intervalo_y'].unique()

# Cria um gráfico para cada valor de intervalo_x
for intervalo_x in intervalo_x_values:
    # Filtra os dados para o intervalo_x atual
    subset_x = data[data['intervalo_x'] == intervalo_x]

    # Configura o gráfico
    plt.figure(figsize=(12, 8))

    # Define a largura das barras e a posição inicial
    bar_width = 0.15  # Largura das barras
    spacing = 0.05     # Espaçamento entre as barras
    index = np.arange(len(numero_threads_values))  # Baseia o índice no número de numero_threads

    # Cria um loop para cada valor de intervalo_y
    for i, y in enumerate(intervalo_y_values):
        # Filtra os dados para o intervalo_y atual
        subset = subset_x[subset_x['intervalo_y'] == y]

        # Cria uma lista para armazenar os tempos
        tempos = []

        # Obtém os tempos correspondentes para cada numero_threads
        for th in numero_threads_values:
            th_subset = subset[subset['numero_threads'] == th]
            tempo = th_subset['tempo'].values[0] if not th_subset.empty else 0
            tempos.append(tempo)

        # Plota as barras para o intervalo_y atual
        plt.bar(index + i * (bar_width + spacing), tempos, bar_width, label=f'intervalo_y = {y}')

    # Adiciona título e rótulos aos eixos
    plt.title(f'Distribuição dos Tempos de Execução para intervalo_x = {intervalo_x} (escala logaritimica)')
    plt.xlabel('Número de Threads')
    plt.ylabel('Tempo de Execução (log(s))')

    # Define o eixo Y em escala logarítmica
    plt.yscale('log')

    # Ajusta os rótulos do eixo X
    plt.xticks(index + (bar_width + spacing) * (len(intervalo_y_values) - 1) / 2, numero_threads_values)

    plt.legend(title="Intervalo_y")
    plt.grid(axis='y', alpha=0.75)

    # Salva e exibe o gráfico
    plt.savefig(f"histograma_tempos_execucao_intervalo_x_{intervalo_x}_log.png")
    plt.show()
