
# 6. Generar un gráfico de tipo barras que compare películas vs series
# desde el 2010 hasta el 2021. El resultado del grafico debe ser algo asi:
import pandas
import matplotlib.pyplot as plt

index = []
progreso_iniciar = 2010
fecha_max = 2021

#entrada de los datos
entrada = pandas.DataFrame(pandas.read_csv("netflix_titles.csv"))

#series 1 con los objetos
s1 = entrada[entrada["type"] == "Movie"]
s2 = entrada[entrada["type"] == "TV Show"]

#creaccion del index o la imformacion horizontal
while progreso_iniciar <= fecha_max:
    index.append(progreso_iniciar)
    progreso_iniciar += 1


sujetos = {"Movies":s1.groupby("release_year").size(), "TV Show":s2.groupby("release_year").size()} 
salida = pandas.DataFrame(sujetos, index=index)
graphicBar = salida.plot.bar(rot = 0)
plt.show()

# print(s1)




