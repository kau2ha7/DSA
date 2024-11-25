class Graph:
    def __init__(self,vno):
        self.vertex_count = vno 
        self.adj_list = [[0] * vno for v in range(vno)]
    def add_edge(self,u,v,weight=0):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u][v] = weight
            self.adj_list[v][u] = weight
        else:
            print('invalid vertex')
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u][v] = 0
            self.adj_list[v][u] = 0
        else:
            print('invalid vertex')
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_list[u][v] != 0
    def print_edge(self):
        for row_list in self.adj_list:
            print(' '.join(map(str,row_list)))



g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2, 3)
g.add_edge(1, 3)
g.remove_edge(0, 1)

g.print_edge()

print(g.has_edge(1, 3))  # Should return True
print(g.has_edge(0, 1))  # Should return False
        