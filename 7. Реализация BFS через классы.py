class Node:
    def __init__(self, value):
        self.value = value
        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'

    def __repr__(self):
        return f'Node({self.value})'


class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        if self._root is None:
            return []

        stack = [self._root]
        visited = []
        visited_set = set()

        while stack:
            current_node = stack.pop()

            if current_node not in visited_set:
                visited.append(current_node)
                visited_set.add(current_node)

                for neighbor in reversed(current_node.outbound):
                    if neighbor not in visited_set:
                        stack.append(neighbor)

        return visited

    def bfs(self):
        if self._root is None:
            return []

        queue = [self._root]
        visited = []
        visited_set = set()
        visited_set.add(self._root)

        while queue:
            current_node = queue.pop(0)
            visited.append(current_node)

            for neighbor in current_node.outbound:
                if neighbor not in visited_set:
                    queue.append(neighbor)
                    visited_set.add(neighbor)

        return visited


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
k = Node('k')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
a.point_to(e)
e.point_to(f)
e.point_to(g)
f.point_to(i)
f.point_to(h)
g.point_to(k)

g = Graph(a)

print(g.dfs())
print(g.bfs())