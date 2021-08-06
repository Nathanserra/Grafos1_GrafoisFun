#Resposta questão 2

class Grafo:
    def __init__(self, V, E):
        self.V = V
        self.E = set(frozenset((u,v)) for u,v in E)
        self._vizinhos = {}
        
        for v in V:
            self.adiciona_vertice(v)

        for u,v in self.E:
            self.adiciona_aresta(u,v)
    
    def adiciona_vertice(self, v):
        if v not in self._vizinhos:
            self._vizinhos[v] = set()

    def adiciona_aresta(self, u, v):
        self.adiciona_vertice(u)
        self.adiciona_vertice(v)
        self.E.add(frozenset([u,v]))
        self._vizinhos[u].add(v)
        self._vizinhos[v].add(u)

    def adiciona_aresta_direcionada(self, u, v):
        self.adiciona_vertice(u)
        self.adiciona_vertice(v)
        self.E.add(frozenset([u,v]))
        self._vizinhos[u].add(v)
    
    def apaga_aresta(self, u, v):
        e = frozenset([u,v])
        if e in self.E:
            self.E.remove(e)
            self._vizinhos[u].remove(v)
            self._vizinhos[v].remove(u)
    
    def apaga_vertice(self, u):
        para_apagar = list(self.vizinhos(u))
        for v in para_apagar:
            self.apaga_aresta(u,v)
        del self._vizinhos[u]
    
    def existe_aresta(self, u, v):
        e = frozenset([u,v])
        if e in self.E:
            return True
        else:
            return False

    def deg(self, v):
        return len(self._vizinhos[v])

    def vizinhos(self, v):
        return iter(self._vizinhos[v])

    @property
    def m(self):
        return len(self.E)
    
    @property
    def n(self):
        return len(self._vizinhos)    

    
    def DFS_retorna_ciclo(self):
        G_aux = Grafo(self.V,{})
        G_ciclo = Grafo(self.V,{})

        nao_visitados = self.V
        for v in self.V:
            if v in nao_visitados:
                self.DFS_visit(G_ciclo, G_aux, v, nao_visitados)

        return G_ciclo

    def DFS_visit(self, G_ciclo, G_aux, v,nao_visitados):
        nao_visitados.remove(v)
        if(G_ciclo.m > 0):
            return

        for w in list(self.vizinhos(v)):
            if w in nao_visitados:
                G_aux.adiciona_aresta_direcionada(w,v)
                self.DFS_visit(G_ciclo, G_aux, w,nao_visitados)
        
            if (w not in nao_visitados) and (not G_aux.existe_aresta(w,v)) and (G_ciclo.m == 0):
                G_ciclo.adiciona_aresta(v,w)
                self.acha_ciclo(G_ciclo, G_aux, w, v)


    def acha_ciclo(self,G_ciclo, G_aux, w, v):
            if v != w:
                G_ciclo.adiciona_aresta(list(G_aux.vizinhos(v))[0],v)
                self.acha_ciclo(G_ciclo, G_aux, w, list(G_aux.vizinhos(v))[0])

if __name__ == '__main__':
    G = Grafo([1,2,3,4,5,6,7,8,9,10,11], {(1,2),(2,3),(3,4),(3,5),(4,8),(5,6),(6,7),(7,8),(7,9),(9,11),(11,10),(10,8)})
    G1 = G.DFS_retorna_ciclo()
    for i in range(G1.n):
        print(f'{i+1}: ', end=' ')
        print(list(G1.vizinhos(i+1)))