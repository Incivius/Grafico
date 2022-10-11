# importando matplitlib
from ast import NodeTransformer
from turtle import color
import matplotlib.pyplot as plt 

fig = plt.figure()
ax = fig.add_subplot(111)


# declarando as listas com os valores que serão usados no gráfico
criterio = ["trbalho em equipe", "produtividade", "depressão", "anciedade", "vontade de viver"]
sprint = [2, 3, 4, 1, 5]
sprint2 = [3, 1, 4, 5, 1]

# titulo do gráfico
plt.title("Primeiro gráfico")

ax.set_ylim([0, 5.2])

# adicionando labels no eixo x e y
plt.xlabel("valores postos")
plt.ylabel("meses postos")

# inicializando a tela com o gráfico
plt.bar(criterio, sprint, color = "red")
plt.bar(criterio, sprint2, color = "purple")
plt.show()
