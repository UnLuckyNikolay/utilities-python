from collections.abc import Hashable


class Graph:
    """Barebones version of a graph using an adjacency list."""

    def __init__(self):
        self._graph = {}

    def __repr__(self):
        result = ""
        for kvpair in sorted(self._graph.items(), key=lambda x: x[0]):
            if len(kvpair[1]) == 0:
                result += f"{kvpair[0]}: " + "{}\n"
            else:
                result += f"{kvpair[0]}: {kvpair[1]}\n"
        return result


    def add_edge(self, u : Hashable, v : Hashable):
        """Add an edge with selected coordinates to the graph."""

        if u < 0 or v < 0:
            raise ValueError("Vertices should be positive or zero.")
        
        if u not in self._graph:
            self._graph[u] = set()
        if v not in self._graph:
            self._graph[v] = set()

        self._graph[u].add(v)
        self._graph[v].add(u)

    def delete_edge(self, u : Hashable, v : Hashable):
        """Remove an edge with selected coordinates from the graph."""

        if u < 0 or v < 0:
            raise ValueError("Vertices should be positive or zero.")
        
        if u not in self._graph or v not in self._graph:
            return

        if u in self._graph[v] and v in self._graph[u]:
            self._graph[u].remove(v)
            self._graph[v].remove(u)

    def edge_exists(self, u : Hashable, v : Hashable) -> bool:
        """Check if an edge exists at selected coordinates."""

        if u in self._graph and v in self._graph:
            return u in self._graph[v] and v in self._graph[u]
        return False
    
    def get_adjacent_nodes(self, node : Hashable) -> set:
        """Retuns a set of nodes adjacent to the given node."""

        if node in self._graph:
            return self._graph[node]
        raise KeyError(f"{node} is not present in the graph.")
    
    def get_unconnected_vertices(self) -> list:
        """Returns a list of unconected vertices."""

        result = []
        for pair in self._graph.items():
            if len(pair[1]) == 0:
                result.append(pair[0])
        return result
    
    def breadth_first_search(self, start_vertex : Hashable) -> list:
        visited = []
        queue = []
        queue.append(start_vertex)

        while len(queue) > 0:
            current = queue.pop(0)
            visited.append(current)
            for neigh in sorted(self._graph[current]):
                if neigh not in visited and neigh not in queue:
                    queue.append(neigh)

        return visited
    
    def depth_first_search(self, start_vertex : Hashable) -> list:
        if start_vertex not in self._graph:
            raise ValueError(f"{start_vertex} is not present in the graph.")

        visited = []

        self._depth_first_search_inner_rec(visited, start_vertex)

        return visited


    def _depth_first_search_inner_rec(self, visited : list, current_vertex : Hashable) -> list:
        """Inner recursive function for depth_first_search"""

        visited.append(current_vertex)
        for neigh in sorted(self._graph[current_vertex]):
            if neigh not in visited:
                self._depth_first_search_inner_rec(visited, neigh)


class GraphMatrix:
    """Barebones version of a graph using an adjacency matrix."""

    def __init__(self, num_vertices):
        self._graph = []
        for i in range(num_vertices):
            row = []
            for j in range(num_vertices):
                row.append(False)
            self._graph.append(row)

    def __repr__(self):
        lists = ""
        for l in self._graph:
            lists += f"    {l}\n"
        return f"[\n{lists}]"


    def add_edge(self, u : int, v : int):
        """Add edge with selected coordinates to the graph."""

        self._graph[u][v] = True
        self._graph[v][u] = True

    def delete_edge(self, u : int, v : int):
        """Remove an edge with selected coordinates from the graph."""

        self._graph[u][v] = False
        self._graph[v][u] = False

    def edge_exists(self, u : int, v : int) -> bool:
        """Check if an edge exists at selected coordinates."""

        if (
            u < 0 
            or v < 0
            or u > len(self._graph) 
            or v > len(self._graph)
        ):
            raise ValueError(f"({u}, {v}): vertices are out of the dimensions of the graph.")
        
        return self._graph[u][v]