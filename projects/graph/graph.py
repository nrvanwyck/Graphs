"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if (v1 in self.vertices) and (v2 in self.vertices):
            self.vertices[v1].add(v2)
        elif v1 not in self.vertices:
            raise Exception('v1 not in graph!')
        else:
            raise Exception('v2 not in graph!')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        bft_path = []

        vertex_color_dict = {}
        for vertex in self.vertices:
            vertex_color_dict[vertex] = 'white'

        vertex_queue = Queue()
        vertex_queue.enqueue(starting_vertex)
        vertex_color_dict[starting_vertex] = 'gray'
        bft_path.append(starting_vertex)

        while vertex_queue.size() > 0:
            head_vertex = vertex_queue.queue[0]

            for neighbor in self.get_neighbors(head_vertex):
                if vertex_color_dict[neighbor] == 'white':
                    vertex_queue.enqueue(neighbor)
                    vertex_color_dict[neighbor] = 'gray'
                    bft_path.append(neighbor)

            vertex_queue.dequeue()
            vertex_color_dict[head_vertex] = 'black'

        print(bft_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        dft_path = []

        vertex_color_dict = {}
        vertex_parent_dict = {}
        for vertex in self.vertices:
            vertex_color_dict[vertex] = 'white'
            vertex_parent_dict[vertex] = None

        vertex_stack = Stack()
        vertex_stack.push(starting_vertex)

        while vertex_stack.size() > 0:
            head_vertex = vertex_stack.pop()

            if vertex_color_dict[head_vertex] == 'white':
                vertex_color_dict[head_vertex] = 'gray'
                dft_path.append(head_vertex)

                for neighbor in self.get_neighbors(head_vertex):
                    vertex_stack.push(neighbor)
                    vertex_parent_dict[neighbor] = head_vertex

            vertex_color_dict[head_vertex] = 'black'

        print(dft_path)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        dft_path = []

        vertex_color_dict = {}
        vertex_parent_dict = {}
        for vertex in self.vertices:
            vertex_color_dict[vertex] = 'white'
            vertex_parent_dict[vertex] = None

        for vertex in self.vertices:
            if vertex_color_dict[vertex] == 'white':

                def dft_recursive_visit(vertex):
                    """
                    Helper function for dft_recursive
                    """
                    vertex_color_dict[vertex] = 'gray'
                    dft_path.append(vertex)

                    for neighbor in self.get_neighbors(vertex):
                        if vertex_color_dict[neighbor] == 'white':
                            vertex_parent_dict[neighbor] = vertex
                            dft_recursive_visit(neighbor)

                    vertex_color_dict[vertex] = 'black'

                dft_recursive_visit(vertex)

        print(dft_path)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        dfs_path = []

        vertex_color_dict = {}
        vertex_parent_dict = {}
        for vertex in self.vertices:
            vertex_color_dict[vertex] = 'white'
            vertex_parent_dict[vertex] = None

        vertex_stack = Stack()
        vertex_stack.push(starting_vertex)

        while vertex_stack.size() > 0:
            head_vertex = vertex_stack.pop()

            if vertex_color_dict[head_vertex] == 'white':
                vertex_color_dict[head_vertex] = 'gray'
                dfs_path.append(head_vertex)
                if head_vertex == destination_vertex:
                    return dfs_path

                for neighbor in self.get_neighbors(head_vertex):
                    vertex_stack.push(neighbor)
                    vertex_parent_dict[neighbor] = head_vertex

            vertex_color_dict[head_vertex] = 'black'

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None,
                      path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(
                    child_vert, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
