import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
    'Vendas': [100, 120, 150, 180, 200],
    'Lucro': [500, 600, 700, 800, 900]
}
df = pd.DataFrame(dados)
df.to_csv('dados_vendas.csv', index=False)

df = pd.read_csv('dados_vendas.csv')

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Análise de Vendas e Lucro', fontsize=16)

axs[0, 0].pie(df['Vendas'], labels=df['Mês'], autopct='%1.1f%%', startangle=90)
axs[0, 0].set_title('Distribuição de Vendas')

axs[0, 1].scatter(df['Vendas'], df['Lucro'], color='green')
axs[0, 1].set_title('Vendas x Lucro')
axs[0, 1].set_xlabel('Vendas')
axs[0, 1].set_ylabel('Lucro')
axs[0, 1].grid(True)

axs[1, 0].bar(df['Mês'], df['Vendas'], color='skyblue')
axs[1, 0].set_title('Vendas por Mês')
axs[1, 0].set_xlabel('Mês')
axs[1, 0].set_ylabel('Vendas')

axs[1, 1].plot(df['Mês'], df['Lucro'], marker='o', color='orange')
axs[1, 1].set_title('Evolução do Lucro')
axs[1, 1].set_xlabel('Mês')
axs[1, 1].set_ylabel('Lucro')
axs[1, 1].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
