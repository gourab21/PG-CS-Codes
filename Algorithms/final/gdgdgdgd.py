def do(s):
    s=s.split('\n')
    for i in range(1,len(s)+1):
        print(i,".",s[i-1])


s="""       Initialize an empty set visited to track visited vertices
        Initialize a list queue and add start_vertex to it
        Initialize an empty list bfs_order to store the BFS traversal order
        While queue is not empty:
                Dequeue the first vertex from the queue into current
                If current is not in visited:
                        Mark current as visited
                        Append current to bfs_order
                        For each neighbor of current in graph[current]:
                                If neighbor is not in visited:
                                        Enqueue neighbor into queue
        Return bfs_order
"""

do(s)