import requests
import matplotlib.pyplot as plt
url = "https://sistema-votos-python.vercel.app/planillaVotos"

#Obtención de data
data = requests.get(url).json()

#Definimos función de conteo de votos
"""
Funciona seleccionado la id y pasandole la información en el formato lista (asi lo devuelve la api).
Luego, iteramos en la data. Si la id buscada coincide con una de las ids devuelta por la API suma un voto al conteo. Al final de iterar toda la data devuelve la suma de todos los votos de esa id en partícular
"""
def conteoVotos(id:str, data:list):
    res = 0
    id = str(id)
    for item in data:
        if item["ID"] == id:
            res += 1
    return res

"""
Gráficamos los contenedores. Fácil, verdad? xd
"""
def graficar(titulos:list, valores:list):
    
    fig, ax = plt.subplots()
    ax.pie(titulos, labels=valores)
    plt.show()


"""
ACá se definen los contenedores para los valores. Para iterar cada stand, por ahora, lo pensé de esta manera. Iteramos un rango desde 1 (primer stand) hasta N (último stand) y llamamos a la función contar voto. Por último, si el voto es distinto de 0, es decir que hay votos, se los pasamos a los contenedores para luego graficar
"""
titulos = []
valores = []
for stand in range(1,50):
    
    if not conteoVotos(stand, data) == 0:    
        titulos.append(stand)
        valores.append(conteoVotos(stand, data))

graficar(titulos,valores)