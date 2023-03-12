import random
from Cidade import Cidade
from Util import instanciarCidades
from Util import calcularDistanciaCidades

# CONCEITOS BUSCA TABU:
# A BUSCA TABU É UM MÉTODO DE OTIMIZAÇÃO HEURÍSTICA QUE VISA ENCONTRAR A SOLUÇÃO
# ÓTIMA PARA UM PROBLEMA DE OTIMIZAÇÃO. ELE É BASEADA EM UM PROCESSO ITERATIVO QUE
# EXPLORA O ESPAÇO DE SOLUÇÕES EM BUSCA DE UMA SOLUÇÃO MELHOR DO QUE A ATUAL

# PROBLEMA:
# O PROBLEMA ESCOLHIDO PARA OTIMIZAÇAO FOI O PROBLEMA DO CAIXEIRO VIAJANTE
# NÓS ESCOLHEMOS 7 CIDADES DO PARANÁ E PEGAMOS SUAS COORDENADAS, COM ISSO
# QUEREMOS DESCOBRIR QUAL É O MENOR TRAJETO O POSSÍVEL PASSANDO POR TODAS ELAS

# AUTORES:
# GABRIEL CRESPO BISCAIA         RA 118928
# GABRIEL RODRIGUES DE SOUZA     RA 118038
# PEDRO HENRIQUE ROMANO ZAFALON  RA 120117


def printarSolucao(solucao):
    print("[ ", end="")
    for i in range(len(solucao)):
        if i == len(solucao)-1:
            print(solucao[i].getNome(), "", end="")
        else:
            print(solucao[i].getNome(), ", ", end="")
    print(" ]  Distancia Solucao = ",
          calcularDistanciaTotalSolucao(solucao), "Km")


def printarSolucoes(lista_solucoes):
    for solucao in lista_solucoes:
        printarSolucao(solucao)
        print("\n\n")


def calcularDistanciaTotalSolucao(solucao):
    distancia = 0

    for i in range(len(solucao)):
        if i == (len(solucao)-1):
            distancia += calcularDistanciaCidades(solucao[i], solucao[0])
        else:
            distancia += calcularDistanciaCidades(solucao[i], solucao[i+1])

    return distancia


def pegarMenorDistancia(lista_solucoes):
    # melhor solução
    melhor = None
    # melhor valor
    melhor_valor = None

    for solucao in lista_solucoes:
        valor_solucao_atual = calcularDistanciaTotalSolucao(solucao)

        if melhor_valor == None:
            melhor = solucao
            melhor_valor = valor_solucao_atual
        elif valor_solucao_atual < melhor_valor:
            melhor_valor = valor_solucao_atual
            melhor = solucao

    return melhor


# instancia as cidades
cidades = instanciarCidades()

# forma uma solução aleatoria para o problema do caixeiro viajante
random.shuffle(cidades)

# limite de iteracoes para encontrar solucao
max_iteracoes = 10
num_iteracoes = 0

# limite da lista tabu
tam_lista_tabu = 3
lista_tabu = []

# solucao inicial (pegando a solucao aleatoria após o shuffle)
solucao_atual = cidades
melhor_solucao = solucao_atual

print("Problema Caixeiro Viajante utilizando Busca Tabu!!\nSolucao para caminho usando estas CIDADES...")

for cidade in cidades:
    print(cidade.getNome(), " ")
print("\n")

print("SOLUCAO INICIAL: ")
printarSolucao(solucao_atual)
print("\n")

print("DESENVOLVIMENTO ALGORITMO: ")
while (num_iteracoes < max_iteracoes):
    printarSolucao(solucao_atual)
    solucoes_vizinhas = []

    # Utilizando o método SWAP para selecionar as soluções vizinhas a solução atual
    # Método SWAP inverte a posição de dois elementos apenas (uma pequena mudança)

    for i in range(len(cidades)-1):
        j = i+1
        for j in range(len(cidades)):
            solucao = []
            for aux in solucao_atual:
                # Instancia o array para calculo da solucao vizinha
                solucao.append(Cidade(aux.getNome(), aux.getX(), aux.getY()))

            solucao[i], solucao[j] = Cidade(solucao[j].getNome(), solucao[j].getX(
            ), solucao[j].getY()), Cidade(solucao[i].getNome(), solucao[i].getX(), solucao[i].getY())  # Esta linha inverte os dois elementos i, j = j, i
            solucoes_vizinhas.append(solucao)

    # verificar se esta no tabu
    # Solucoes peneiradas dizem respeito as solucoes que não estão na lista tabu,
    # evitando que fiquem presas em um ótimo local
    solucoes_peneiradas = []

    for solucao in solucoes_vizinhas:
        if solucao not in lista_tabu:
            solucoes_peneiradas.append(solucao)

    if len(solucoes_peneiradas) > 0:
        # pega a que tem o melhor resultado, ou seja menor distancia da rota

        solucao_atual = pegarMenorDistancia(solucoes_peneiradas)

        # se a solucao for melhor que a melhor_solucao entao substitui e coloca ela
        # como nova melhor solucao
        if solucao_atual != None and calcularDistanciaTotalSolucao(solucao_atual) < calcularDistanciaTotalSolucao(melhor_solucao):
            if len(lista_tabu) == tam_lista_tabu:
                # se a lista_tabu tiver em seu tamanho limite, tire o primeiro elemento, como se fosse um FIFO
                lista_tabu.pop(0)

            lista_tabu.append(solucao_atual)

            melhor_solucao = solucao_atual

            num_iteracoes = 0  # reseta o num_iteracoes pois encontrou uma solucao melhor que a anterior
        else:
            # nao encontrou entao aumenta o num_iteracoes afim de limitar e nao ficar infinitamente no loop
            num_iteracoes += 1

print("\nLISTA TABU -> TAM = ", tam_lista_tabu)
for solucao in lista_tabu:
    printarSolucao(solucao)

print("\nMELHOR SOLUCAO: ")
printarSolucao(melhor_solucao)
