# Playing around with classes
import random
import math
import numpy

class Graph:
    # Initializing what a (weighted) graph is, where weights are the third coordinate of edges if they exist
    # Weights are assumed to be 1 if not specified otherwise
    def __init__(self, vertices=set([]), edges=set([])):
        self._vertices = vertices
        self._edges = edges

    # Defining a new property of the graph: Its adjacency matrix
    # Note the adjacency matrix gets majorly screwed up if you don't index your vertices as 0, 1, 2, ..., n
    def adjacency(self):

        # Since I'm not using numpy, I'm making the matrix with nested lists
        adjacency_matrix = []
        row = []
        for i in range(0, len(self._vertices)):
            row.append(0)
        for j in range(0, len(self._vertices)):
            adjacency_matrix.append(row[:])
        # One must put row[:] to create a separate instance of "row" that is unique
        # Else, changing one entry in the matrix changes that entry in every row,
        # As the matrix's rows would then be the same object.

        for edge in self._edges:
            v1 = edge[0]
            v2 = edge[1]
            try:
                adjacency_matrix[v1][v2] = edge[2]
                adjacency_matrix[v2][v1] = edge[2]
            except:
                adjacency_matrix[v1][v2] = 1
                adjacency_matrix[v2][v1] = 1
        # This sets entries to 1 where the entry corresponds to an edge between the row index and column index

        return adjacency_matrix

    #Identical to the above, but treats an edge (i,j) as an arrow i -> j instead:
    def directed_adjacency(self):
        # Since I'm not using numpy, I'm making the matrix with nested lists
        adjacency_matrix = []
        row = []
        for i in range(0, len(self._vertices)):
            row.append(0)
        for j in range(0, len(self._vertices)):
            adjacency_matrix.append(row[:])
        # One must put row[:] to create a separate instance of "row" that is unique
        # Else, changing one entry in the matrix changes that entry in every row,
        # As the matrix's rows would then be the same object.

        for edge in self._edges:
            v1 = edge[0]
            v2 = edge[1]
            try:
                adjacency_matrix[v1][v2] = edge[2]
            except:
                adjacency_matrix[v1][v2] = 1
        # This sets entries to 1 where the entry corresponds to an edge between the row index and column index

        return adjacency_matrix

    # Defining a new property of each vertex of the graph: Its adjacent edges
    def adjacent_vertices(self, vertex):
        if vertex in self._vertices:
            adjacentlist = []
            for edge in self._edges:
                if edge[0] == vertex:
                    try:
                        adjacentlist.append((edge[1],edge[2]))
                    except:
                        adjacentlist.append((edge[1],1))
                elif edge[1] == vertex:
                    try:
                        adjacentlist.append((edge[0],edge[2]))
                    except:
                        adjacentlist.append((edge[0],1))

            return adjacentlist
        else:
            print("That is not a vertex")
            return

    #Identical to the above, but treats the edge (i,j) as an arrow i -> j instead:
    def directed_adjacent_vertices(self, vertex):
        if vertex in self._vertices:
            adjacentlist = []
            for edge in self._edges:
                if edge[0] == vertex:
                    try:
                        adjacentlist.append((edge[1], edge[2]))
                    except:
                        adjacentlist.append((edge[1],1))
            return adjacentlist
        else:
            print("That is not a vertex")
            return



    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges

#n: Max number of vertices
#r2: Probability of a given arrow existing (remember there's roughly n^2 edges in a complete graph!)
def random_graph(n,r2):
    try:
        # Uniformly distributed random number of vertices between 1 and n
        r = random.randint(1, n)
        v = set([])
        for i in range(0, r):
            v.add(i)

        # Randomly picking edge
        e = set([])
        for j in v:
            for k in v:
                if random.random() < r2 and k != j:
                    e.add((j, k))

        g = Graph(vertices=v, edges=e)
        return g
    except:
        return

#Identical to the above, but checks if an edge already exist so there's no duplicates
def random_undirected_graph(n,r2):
    try:
        # Uniformly distributed random number of vertices between 1 and n
        r = random.randint(1, n)
        v = set([])
        for i in range(0, r):
            v.add(i)

        # Randomly picking edge
        e = set([])
        for j in v:
            for k in v:
                if random.random() < r2 and k != j and (j,k) not in e:
                    e.add((j, k))

        g = Graph(vertices=v, edges=e)
        return g
    except:
        return

#Identical to above, but for a weighted graph. w is a weight constant: each arrow is given a weight
#with average weight w.
#If w is an integer, weights are Poisson-distributed.
#If w is a float, weights are "Normally-distributed with mean w, st dev sqrt(w)"...
#...except that wouldn't work because weights need to be positive!
#Turns out (thanks Wikipedia) that the sum of uniform distributions nicely approximates the normal distribution
#Not only by CLT but also because it's a spline approximation! How neat! Irwin-Hall is the distribution.
#Not only that, but it's supposedly computationally efficient to approximate the normal distribution in such a fashion
#Not only that, but it also has cutoffs the way I'd like it to!
def random_weighted_graph(n,r2,w):
    try:

        rw = False
        if type(w) != int:
            rw = True

        # Uniformly distributed random number of vertices between 1 and n
        r = random.randint(1, n)
        v = set([])
        for i in range(0, r):
            v.add(i)

        # Randomly picking edge
        e = set([])
        for j in v:
            for k in v:
                if random.random() < r2 and k != j:
                    if rw == False:
                        #Randomly assigning weights, poisson distributed with mean w in the int case (Z-valued)
                        e.add((j,k,numpy.random.poisson(w)))
                    else:
                        #Randomly assigning weights, Irwin-Hall distributed with mean w in the float case (R-valued)
                        r1 = 0
                        for i in range(0,math.ceil(2*w)):
                            r1 += random.random()
                        e.add((j,k,r1))


        g = Graph(vertices=v, edges=e)
        return g
    except:
        return


def main():
    #Generates and then prints a random weighted graph
    g0 = random_weighted_graph(20,0.3,3)

    print(g0.vertices)
    print(g0.edges)


if __name__ == '__main__': main()
