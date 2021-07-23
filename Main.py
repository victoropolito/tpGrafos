# coding: utf-8

import _tkinter
import os
import sys

# colocar arquivo de entrada
# função que lê o arquivo e transforma em lista/matriz
def le_arquivo():
    arq = open('example.txt', 'r')
    FirstLine = arq.readline().rstrip()
    FirstLine = FirstLine.split()
    print(arq)
    print(FirstLine)
    Vertices = int(FirstLine[0])
    Arestas = int(FirstLine[1])
    print(Vertices)
    print(Arestas)
    Matriz = [[0 for _ in range(Vertices)] for _ in range(Vertices)]
    print(Matriz)
    Lista = [[] for x in range(Vertices)]
    print(Lista)
    Peso = [[] for i in range(0, Arestas)]
    print(Peso)

    for i in range(0, Arestas):
        Aresta = arq.readline()
        print()
        print(Aresta)
        Aresta = Aresta.split(" ")
        print(Aresta)
        x = int(Aresta[0])
        print(x)
        y = int(Aresta[1])
        print(y)
        z = int(Aresta[2])
        print(z)
        Lista[x].append((y, z))
        Lista[y].append((x, z))
        Matriz[x][y] = z
        Matriz[y][x] = z
        Peso[i] = z

    for i in range(0, Vertices):
        print   

    # FUNÇÃO DE MAIOR/MENOR GRAU, MEDIA E FRENQUENCIA RELATIVA
    
    # TO-DO INDICAR VÉRTICE DO MAIOR/MENOR GRAU
    grau_maior = Peso[0]
    grau_menor = Peso[0]
    grau_soma = 0
    grau_media = 0
    freq_rel_maior = 0
    freq_rel_menor = 0
    qntd_vertices_maior = 1
    qntd_vertices_menor = 1

    # algoritmo que identifica maior/menor grau e calcula media
    for i in range(0, Arestas):
        if (Peso[i] > grau_maior):
            grau_maior = Peso[i]
        elif (Peso[i] < grau_menor):
            grau_menor = Peso[i]
        grau_soma += Peso[i]
        grau_media = (grau_soma / Arestas)
    # algoritmo que calcula a freq. relativa
    for i in range(0, Arestas):
        if (grau_maior == Peso[i]):
            qntd_vertices_maior += 1
        if (Peso[i] == grau_menor):
            qntd_vertices_menor += 1
        freq_rel_maior = (qntd_vertices_maior / Vertices)
        freq_rel_menor = (qntd_vertices_menor / Vertices)

    #sequencia de prints
    print(f"Maior grau: {grau_maior} - Vertice: ")
    print(f"Menor grau: {grau_menor} - Vertice: ")
    print(f"Grau medio: {grau_media}")
    print(f"Freq. relativa {grau_maior}: {freq_rel_maior}")
    print(f"Freq. relativa {grau_menor}: {freq_rel_menor}")
    print("-----------------------------------------------")

    # forma_de_apresentacao = input('Digite qual sera a forma de representacao do grafo (Lista/Matriz): ')

G = [
    [1, 4],
    [0, 4],
    [3],
    [2],
    [0, 1],
]

# FUNÇÃO DE BUSCA EM LARGURA
# passar um grafo e o vertice de começo
def busca_largura(G, s):
    desc = [0 for i in range(len(G))] 
    nivel = [-1 for i in range(len(G))]
    Q = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(Q) != 0:
        u = Q.pop(0)
        for v in G[u]:
            if desc[v] == 0:
                Q.append(v)
                R.append(v)
                desc[v] = 1
                nivel[v] = nivel[u] + 1
    nivel_filtrado = list(filter(lambda x: x>-1, nivel))
    print("#vertice:nivel")
    for i in range(len(R)):
        print(f"{R[i]}:{nivel_filtrado[i]}")
    return R

# FUNÇÃO DE BUSCA EM PROFUNDIDADE

def busca_prufundidade(G, s):
    desc = [0 for i in range(len(G))]
    nivel = [-1 for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for v in G[u]:
            if desc[v] == 0:
                desempilhar == False
                S.append(v)
                nivel[v] = len(R)
                R.append(v)
                desc[v] = 1
                break
        if desempilhar:
            S.pop()
    nivel_filtrado = list(filter(lambda x: x>-1, nivel))
    print("#vertice:nivel")
    for i in range(len(R)):
        print(f"{R[i]}:{nivel_filtrado[i]}")
    return R

# FUNÇÃO GRAFO CONEXO/DESCONEXO

comp = [0 for i in range(len(G))]

def componentes_conexas(G):
    marca = 0
    lista_aux = [1 for i in range(len(G))]
    for u in range(len(G)):
        if comp[u] == 0:
            marca+=1
            print(marca)
            busca_profundidade_rec(G,u, marca)
    
    return comp

def busca_profundidade_rec(G, s, marca):
    comp[s] = marca
    for v in G[s]:
        if comp[v] == 0:
            busca_profundidade_rec(G, v, marca)

#print(componentes_conexas(G))

##################### INICIO DA IDENTAÇÃO ###############################

class Arquivo:
    #Método contrutor da classe
    def __init__(self, arquivo_entrada = None, arquivo_saida = None):
        self.arquivo_entrada = arquivo_entrada
        self.arquivo_saida = arquivo_saida
        #self.vertices = []
        #self.arestas = []
        #self.comandos = []
        #self.grafos = []
        #self.peso = []

    #Função que abre o arquivo e o retorna aberto (default)
    def abrir_arquivo(self, arquivo, modo_abertura):
        return open(arquivo, modo_abertura)

    def ler_arquivo(self):
        arq = self.abrir_arquivo(self.arquivo_entrada, "r")
        lista_dados = arq.readlines()
        arq.close()
        return lista_dados

    def distribui_dados(self, lista):
	    indice_vertice = lista.index("ARESTAS\n")
	    indice_aresta = lista.index("COMANDOS\n")

	    dados = {}
	    dados['grafo'] = []
	    dados['arestas'] = []
	    dados['comandos'] = []

	    for i in lista[1:indice_vertice - 1]:
	    	dados['grafo'].append(i)

	    for i in lista[indice_vertice + 1:indice_aresta - 1]:
	    	dados['arestas'].append(i)

	    for i in lista[indice_aresta + 1:]:
	    	dados['comandos'].append(i)	

	    return dados        

print(le_arquivo())

print(busca_largura(G, 0))