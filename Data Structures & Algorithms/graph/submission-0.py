class Graph:
    
    def __init__(self):
        # create adjacency list
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        # add src as vertex
        if src not in self.graph:
            self.graph[src] = []

        # add dst as a vertex
        if dst not in self.graph:
            self.graph[dst] = []
        
        # add dst as neighbor to src vertex if it isnt
        if dst not in self.graph[src]:
            self.graph[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        # src vertex doesn't exist, therefore edge doesn't exist
        if src not in self.graph:
            return False

        # edge exists, therefore remove edge
        if dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        
        # edge doesn't exist
        return False


    def hasPath(self, src: int, dst: int) -> bool:

        def graphDFS(src: int, dst: int, visited: set) -> bool:
            # end path if vertex already visited
            if src in visited:
                return 0
            # path found
            if src == dst:
                return 1

            # loop through each neighbor
            visited.add(src)
            path = 0
            for neighbor in self.graph[src]:
                path += graphDFS(neighbor, dst, visited)
            visited.remove(src)
            return path


        return True if graphDFS(src, dst, set()) else False






