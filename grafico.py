import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados do arquivo CSV
data = pd.read_csv("resultado.csv")

# Configura o gráfico
plt.figure(figsize=(10, 6))

# Plota os tempos de execução para cada número de threads
for th in data['numero_threads'].unique():
    subset = data[data['numero_threads'] == th]
    plt.plot(
        subset['intervalo_x'] * subset['intervalo_y'], 
        subset['tempo'], 
        marker='o', 
        label=f'{th} Threads'
    )

# Adiciona título e rótulos aos eixos
plt.title('Comparação dos Tempos de Execução')
plt.xlabel('Tamanho do Intervalo (X * Y)')
plt.ylabel('Tempo de Execução (s)')
plt.legend(title="Número de Threads")
plt.grid(True)

# Salva e exibe o gráfico
plt.savefig("comparacao_tempos_execucao.png")
plt.show()
