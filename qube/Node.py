class Node:


    def __init__(self, name=None):
        self.name = name
        self.edges = []
        self.distance = 2729
    

    # adds an edge to the edge list
    def add_edge(self, node, move):
        if node.name == self.name:
            return
        for e in self.edges:
            if node.name == e[0].name:
                return
        to_add = (node, move)
        self.edges.append(to_add)
    

    # removes an edge from the list
    def remove_edge(self, node):
        # if it's not an edge, return
        if node not in self.edges:
            return
        self.edges.remove(node)
    
    # prings the node and its edges
    def print(self):
        # print name
        answer = self.name + ": ["
        # pring edges
        for e in self.edges:
            answer += e[0].name +  ", "
        # formatting and hwaetnot
        if len(self.edges) > 0:
            answer = answer[:-2]
        answer += "]"
        print(answer)
