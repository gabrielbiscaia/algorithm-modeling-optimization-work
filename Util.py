import math
from Cidade import Cidade

# tem que dar pip install requests

#Função que calcula a distancia entre uma cidade origem e a cidade destino (em metros)
def calcularDistanciaCidades(cidade_origem, cidade_destino):
    #usando abs para não resultar em uma distancia negativa
    distanciaX = abs(cidade_origem.getX() - cidade_destino.getX())
    distanciaY = abs(cidade_origem.getY() - cidade_destino.getY())
    # formula de pitagoras para calcular a distancia baseada na distancia absoluta X e Y de duas cidades
    distanciaAbsoluta = math.sqrt(distanciaX**2 + distanciaY**2)

    #Dividindo por 1000 para converter para Km 
    return distanciaAbsoluta/1000

#Função que recebe a latitude e longitude de uma cidade e retorna o ponto cartesiano da (x,y) em que a cidade se encontra na Terra
def mercator(lat, lon):
    R = 6371000  # raio médio da Terra em metros
    x = R * math.radians(lon)
    y = R * math.log(math.tan(math.pi/4 + math.radians(lat)/2))
    return x, y

#Função que faz a chamada da função acima (mercator) para instanciar as cidades
def instanciarCidades():
    cidades = []
# passando a latitude e longitude de cada cidade para a função mercator
    x,y =mercator(-23.4273, -51.9375)
    cidades.append(Cidade('Maringá', x, y))
    x,y =mercator(-23.2927, -51.1732)
    cidades.append(Cidade('Londrina', x, y))
    x,y =mercator(-25.4284, -49.2733)
    cidades.append(Cidade('Curitiba', x, y))
    x,y =mercator(-24.9555, -53.4552)
    cidades.append(Cidade('Cascavel', x, y))
    x,y =mercator(-24.046,  -52.3838)
    cidades.append(Cidade('Campo Mourão', x, y))
    x,y =mercator(-23.5515, -51.4614)
    cidades.append(Cidade('Apucarana', x, y))
    x,y =mercator(-25.0945, -50.1633)
    cidades.append(Cidade('Ponta Grossa', x, y))

    #retornando o array de cidades
    return cidades