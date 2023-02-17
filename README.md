# python_adventures

What I have created so far:



input.py:
 
  This was my second piece of code written!
  
  The code asks for user input of a name, and then a range and a single-variable function to perform the bisection root-finding method on

-----------------------------

graphs.py:
  
  tl;dr: constructed graph data structure, random graph generator

    I create a graph data structure from scratch, including:
      its vertices set, 
      its edges set, 
      its adjacency matrix,
      the adjacency set of a vertex,
      optional weights on edges,
      adjacency matrices and sets can be read as for a directed graph or an undirected graph
    I then create a random directed graph generator with 
      a random number of vertices between 1 and n (avg n/2, naturally), 
      a random collection of edges with likelihood of a given edge r2
    I then do the same but for an undirected graph
    I then do the same but for a weighted and directed graph, where weights are randomly distributed with mean w
      if w is an integer, weights are poisson distributed with lambda = w
      if w is a float, weights are distributed by the sum of uniform random variables from 0 to 2w
      (fun fact: the sum of uniform random variables is called the Irwin-Hall distribution. 
       It is an n-th order spline / piecewise-polynomial approximation of the normal distribution.
       Thanks Wikipedia!)
    Lastly, I run an example of a random weighted directed graph in the main.
 
-----------------------------

random_walk.py:
  
  tl;dr: constructed random walks additively, multiplicatively, and on graphs
    
    This is the culmination of my "intro to python" projects. So far, I have created three random walk functions:
      1-dimension additive and multiplicative mean-free (relative to group identity) random walks: 
        arguments: 
          number of steps in the random walk
          probability of moving to the "right"
          quantity of a movement to the "right"
          initial quantity
        returns:
          a list, the "history" of where the random walker traveled
      Graph random walks:
        arguments:
          number of steps in the random walk
          the graph on which the random walker travels (can be weighted or unweighted) (graph data structure is imported from graphs.py)
          (note this means this code may be incompatible with scipy's graph data structure etc.)
          weight applied
          initial vertex of walk
        returns:
          a list of vertices, the "history" of where the random walker traveled 
    Lastly, I do the following in the main:
      Print the ending values of an additive and a multiplicative random walk
      Print the edges of a random graph called from graphs.py
      Print the history of a random walk on the random graph called above
        
        
   
  
