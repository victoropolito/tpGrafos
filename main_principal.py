Peso_Global = []
Vertices_Global = 0
Arestas_Global = 0


def abrir_arquivo(arquivo, modo_abertura):
    return open(arquivo, modo_abertura)

def grava_arquivo(lista, arquivo_saida):
    arq = abrir_arquivo(arquivo_saida, 'w')
    #for s in arq:
    #    arq.write(str(s) +"\n")
    arq.write(lista)
    arq.close()
    return arq

def acrescenta_arquivo(lista, arquivo_saida, modo_abertura):
    arq = abrir_arquivo(arquivo_saida, 'a')
    arq.write(str(lista))
    arq.close()
    return arq


def gera_lista_sem_peso(arquivo):  # função que gera uma lista global sem os pesos
    arq = abrir_arquivo(arquivo, 'r')

    Cabecalho = arq.readline().rstrip()
    Cabecalho = Cabecalho.split()

    Vertices = int(Cabecalho[0])
    Arestas = int(Cabecalho[1])

    Lista = [[] for x in range(Vertices)]
    #print(Lista)
    for i in range(0, Arestas):
        Aresta = arq.readline()
        Aresta = Aresta.split(" ")
        #print(Aresta)
        x = int(Aresta[0])
        #print(x)
        y = int(Aresta[1])
        #print(y)
        Lista[x].append((y))
        Lista[y].append((x))

    return Lista


'''def gera_matriz_sem_peso(arquivo):
    arq = abrir_arquivo(arquivo, 'r')
    Lista = [[] for x in range(Vertices_Global)]
    for i in range(0, Arestas_Global):
        Aresta = arq.readline()
        Aresta = Aresta.split(" ")
        x = int(Aresta[0])
        y = int(Aresta[1])
        Lista[x].append(y)
        Lista[y].append(x)
    return Lista
'''


def ler_arquivo(arquivo):  # essa função lê o arquivo e converte em lista/matriz
    arq = abrir_arquivo(arquivo, 'r')

    Cabecalho = arq.readline().rstrip()
    Cabecalho = Cabecalho.split()

    Vertices = int(Cabecalho[0])
    Arestas = int(Cabecalho[1])

    global Vertices_Global  # adiciona a variavel global
    Vertices_Global = Vertices

    global Arestas_Global  # adiciona a variavel global
    Arestas_Global = Arestas

    opcao = 0

    while opcao != 2:
        print("[ 1 ] Exibir em matriz" + "\n" + "[ 2 ] Exibir em lista")
        opcao = int(input('>>>>> Qual sua opcao? '))
        print()
        global Peso_Global
        if opcao == 1:  # Exibe em matriz
            Matriz = [[0 for _ in range(Vertices)] for _ in range(Vertices)]
            Peso = [[] for i in range(0, Arestas)]
            for i in range(0, Arestas):
                Aresta = arq.readline()
                Aresta = Aresta.split(" ")
                x = int(Aresta[0])
                y = int(Aresta[1])
                z = int(Aresta[2])
                Matriz[x][y] = z
                Matriz[y][x] = z
                Peso[i] = z
                Peso_Global.append(z)

            return Matriz

        elif opcao == 2:  # Exibe em lista
            Lista = [[] for x in range(Vertices)]
            Peso = [[] for i in range(0, Arestas)]
            for i in range(0, Arestas):
                Aresta = arq.readline()
                Aresta = Aresta.split(" ")
                x = int(Aresta[0])
                y = int(Aresta[1])
                z = int(Aresta[2])
                Lista[x].append((y, z))
                Lista[y].append((x, z))
                Peso[i] = z
                Peso_Global.append(z)

            return Lista

    arq.close()


def calcula_infos(lista):  # essa função calcula as informações do grafo
    grau_maior = Peso_Global[0]
    grau_menor = Peso_Global[0]
    grau_soma = 0
    grau_media = 0
    freq_rel_maior = 0
    freq_rel_menor = 0
    qntd_vertices_maior = 1
    qntd_vertices_menor = 1

    # algoritmo que identifica maior/menor grau e calcula media
    for i in range(0, Arestas_Global):
        if (Peso_Global[i] > grau_maior):
            grau_maior = Peso_Global[i]
            vertice_maior = i - 1
        elif (Peso_Global[i] < grau_menor):
            grau_menor = Peso_Global[i]
            vertice_menor = i - 1
        grau_soma += Peso_Global[i]
        grau_media = (grau_soma / Arestas_Global)

    # algoritmo que calcula a freq. relativa
    for i in range(0, Arestas_Global):
        if (grau_maior == Peso_Global[i]):
            qntd_vertices_maior += 1
        if (Peso_Global[i] == grau_menor):
            qntd_vertices_menor += 1
        freq_rel_maior = (qntd_vertices_maior / Vertices_Global)
        freq_rel_menor = (qntd_vertices_menor / Vertices_Global)

    #for i in range(0, Vertices_Global):                # imprime todos os vertices
    #    print(f"Vertice %s:" % i, lista[i])

    print(f"Maior grau: {grau_maior} - Vertice: {vertice_maior}" +
                 "\n" +
                 f"Menor grau: {grau_menor} - Vertice: {vertice_menor}" +
                 "\n" + f"Grau medio: {grau_media}" + "\n" +
                 f"Freq. relativa {grau_maior}: {freq_rel_maior}" + "\n" +
                 f"Freq. relativa {grau_menor}: {freq_rel_menor}" + "\n" +
                 "-----------------------------------------------")

    #a = gera_lista_sem_peso(lista)
    #b = define_busca(a)


def define_busca(lista): # função de menu para buscas
    opcao = 0
    print("[ 1 ] Buscar em profundidade" + "\n" + "[ 2 ] Buscar em largura")
    opcao = int(input('>>>>> Qual sua opcao? '))
    print()
    if opcao == 1: # busca em produnfidade
        vertice = 0
        print("Em qual vértice deve começar a busca? ")
        vertice = int(input('>>>>> '))
        print()
        busca_prufundidade(lista, vertice)
    elif opcao == 2: # busca em largura
        vertice = 0
        print("Em qual vértice deve começar a busca? ")
        vertice = int(input('>>>>> '))
        print()
        busca_largura(lista, vertice)

def busca_largura(G, s):  # função que percorre o grafo em largura
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
    nivel_filtrado = list(filter(lambda x: x > -1, nivel))
    print()
    print("#vertice:nivel")
    for i in range(len(R)):
        print(f"{R[i]}:{nivel_filtrado[i]}")
    return "Fim da busca"


def busca_prufundidade(G, s):  # função que percorre o grafo em profundidade
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
    nivel_filtrado = list(filter(lambda x: x > -1, nivel))
    print("#vertice:nivel")
    for i in range(len(R)):
        print(f"{R[i]}:{nivel_filtrado[i]}")
    return "Fim da busca"


#TO-DO CONEXAS

def componentes_conexas(lista):
    comp = [0 for i in range(len(lista))]
    marca = 0
    def busca_profundidade_rec(lista, s, marca):
        comp[s] = marca
        for v in lista[s]:
            if comp[v] == 0:
                busca_profundidade_rec(lista, v, marca)
    #lista_aux = [1 for i in range(len(G))]
    for u in range(len(lista)):
        if comp[u] == 0:
            marca += 1
            busca_profundidade_rec(lista, u, marca)
    
    conexas = retorna_conexas(comp)
    print(comp)
    return conexas
    
def retorna_conexas(comp):
    contador_conexas = 0
    #contador_vertices = 0
    for i in range(len(comp)):
        aux = contador_conexas
        if comp[i] != aux:
            contador_conexas += 1

    return contador_conexas

a = ler_arquivo('collaboration_graph.txt')
b = calcula_infos(a)
print(b)
lista = gera_lista_sem_peso('collaboration_graph.txt')
print()
print(define_busca(lista))
#print(lista)
#print(busca_largura(lista, 0))
#print()
#print(busca_prufundidade(lista, 0))
#print()
#grava_arquivo(b,'example_out.txt')
#print(componentes_conexas(lista))
