import matplotlib.pyplot as plt
medias_jose = [10, 5, 8, 9, 10, 5, 4]
meses = ['fev', 'mar', 'abril', 'maio', 'junho', 'julho', 'agosto']

plt.figure()
plt.bar(meses, medias_jose, color='blue')
plt.title('Notas de José por Mês')
plt.xlabel('Mês')
plt.ylabel('Nota')
plt.ylim(0, 10)
plt.show()
