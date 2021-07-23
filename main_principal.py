Peso_Global = []
Vertices_Global = 0
Arestas_Global = 0

def abrir_arquivo(arquivo, modo_abertura):
	return open(arquivo, modo_abertura)

#TO-DO CONVERTER EM LISTA/MATRIZ

def ler_arquivo(arquivo): # essa função lê o arquivo e converte em lista/matriz
    arq = abrir_arquivo(arquivo, 'r')
    Cabecalho = arq.readline().rstrip()
    Cabecalho = Cabecalho.split()

    Vertices = int(Cabecalho[0])
    Arestas = int(Cabecalho[1])
    global Vertices_Global
    Vertices_Global = Vertices
    global Arestas_Global
    Arestas_Global = Arestas

    opcao = 0

    while opcao != 2:
        print("[ 1 ] Exibir em matriz" + "\n" + "[ 2 ] Exibir em lista")
        opcao = int(input('>>>>> Qual sua opcao? '))
        print()
        global Peso_Global
        if opcao == 1:                              # Exibe em matriz
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

        elif opcao == 2:                            # Exibe em lista
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

def calcula_infos(lista): # essa função calcula as informações do grafo
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

    for i in range(0, Vertices_Global):
        print(f"Vertice %s:" % i, lista[i])

    return print(f"Maior grau: {grau_maior} - Vertice: {vertice_maior}" + "\n"
                + f"Menor grau: {grau_menor} - Vertice: {vertice_menor}" + "\n"
                + f"Grau medio: {grau_media}" + "\n"
                + f"Freq. relativa {grau_maior}: {freq_rel_maior}" + "\n"
                + f"Freq. relativa {grau_menor}: {freq_rel_menor}" + "\n"
                + "-----------------------------------------------")

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

a = ler_arquivo('example.txt')
print(calcula_infos(a))

