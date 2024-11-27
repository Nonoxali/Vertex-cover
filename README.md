
This algorithm accepts graphs stored in either matrix or adjacency list format.
We wish to thank Pierre Popineau for the france.gr graph data and overseeeing the project in 2020. 

I) QUICK USE OF THE ALGORITHM

Simply execute the program and use the solve_general(GRAPH) function in the interpreter, which will solve the vertex cover problem and display the answer in a separate window. (GRAPH is a matrix or adjacency list.)

II) USING THE INTERFACE

It is also possible to use the program's interface to quickly access stored graph resolutions.

How to use couvsommet.py to solve the vertex cover of YOUR own graph using the interface:

Just store your graph under a variable in the format of your choice and add it to the dictionary saved_graphs at the top of the code, in the format:

"graph name to display": variable name 				                if your variable is a matrix
"graph name to display": Transfo_Dict_To_Mat(variable name)	  if your variable is a dictionary

These graphs will now be stored in memory and accessible directly from the interface. 

Running the code will launch the interface. Once your desired resolution is chosen, you can either:

- Draw your own graph (under some constraints)
First, choose the vertices and then choose the edges connecting these vertices. You will then have a solution to your graph that will appear in a separate window.

-Choose a graph stored in memory. 
The resolution of this graph will be immediately displayed.

III) VERTEX COVER EXHAUSTIVE METHOD

It is also possible to use the CPS_perfect(graph) function, which only accepts adjacency lists. It is always possible to translate your adjacency matrix into a list using the Mlist() function.

!!! Warning !!!
Beyond 15 vertices, the execution time can become very long due to the algorithm being exponential in complexity with respects to the number of vertices !!

Write "printsolved(lobjr, CPS_perfect(GRAPH)[0])" in the interpreter where GRAPH is the adjacency list of your graph; this will print the perfect resolution of your graph (if completable before the end of the universe).

IV) BONUS
To print a map of metropolitan France and its 226 largest cities, simply execute the second part of the couvsommet.py program. Just modify the PATH0 variable to the one where the france.gr file provided in the zip is stored.

