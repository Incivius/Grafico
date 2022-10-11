# importando matplitlib
from statistics import median
import matplotlib.pyplot as plt

# declarando as listas com os valores que serão usados no gráfico
sprint = ['Sprint1', 'Sprint2', 'Sprint3']

notas1 = [2, 4, 5]
notas2 = [1, 2, 2]
notas3 = [2, 3, 4]
notas4 = [4, 5, 5]
notas5 = [5, 5, 5]

Mnotas1 = int(median(notas1))
Mnotas2 = int(median(notas2))
Mnotas3 = int(median(notas3))
Mnotas4 = int(median(notas4))
Mnotas5 = int(median(notas5))


# titulo do gráfico
plt.title("Primeiro gráfico")

# adicionando labels no eixo x e y
plt.xlabel("valores postos")
plt.ylabel("meses postos")

# inicializando a tela com o gráfico
plt.plot(sprint,Mnotas1)
plt.show()