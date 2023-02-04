from Node import Node

class Graph:


    def __init__(self):
        self.node_list = []


    # adds a node to the graph
    def add_node(self, name=str):
        # try to find it!
        look = self.find_node(name)
        # if it's not null, return. it's already there.
        if look != None:
            return
        # otherwise we add it
        n = Node(name)
        self.node_list.append(n)


    # adds an array of nodes to the graph
    def add_nodes(self, name_list=list):
        for name in name_list:
            self.add_node(name)
    

    # adds an edge to the graph
    def add_edge(self, fro, to, move):
        # finds the from and to nodes
        from_node = self.find_node(fro)
        to_node = self.find_node(to)
        # if one of them isn't there, return
        if from_node == None or to_node == None:
            return
        # otherwise add an edge in one direction
        from_node.add_edge(to_node, move)


    # adds many edges, given starting point and many destinations
    def add_edges(self, fro=str, to_list=list):
        for item in to_list:
            self.add_edge(fro, item)
    

    # removes a node from the graph
    def remove_node(self, name=str):
        # the node that we want to remove
        node = self.find_node(name)
        # if that node doesn't exist, return
        if node == None:
            return
        #remove it from the node list
        self.node_list.remove(node)
        # remove the node from everything in the node list
        for n in self.node_list:
            n.remove_edge(node)
    

    # removes an array of nodes from the graph
    def remove_nodes(self, remove_list=list):
        for name in remove_list:
            self.remove_node(name)
    

    # finds a node and returns it
    def find_node(self, name=str):
        for item in self.node_list:
            if item.name == name:
                return item
    

    # prints the shortest path
    def shortest_path(self, fro=str, to=str):
        path_text = ""
        # get the path (in edges)
        path = self.dijikstra_helper(fro, to)
        # if there's not path, return
        if len(path) == 0:
            print("no, it's empty")
            return
        # add it all to a string
        for p in path:
            path_text += p + " "
        # get the inverse for some reason?
        path_text = self.get_inverse(path_text[:-1])
        # print the instructions
        print(path_text)
        return path_text


    # returns the shortest path as an array of nodes
    def dijikstra_helper(self, fro=str, to=str):
        queue = []
        source = self.find_node(fro)
        dest = self.find_node(to)
        if source == None or dest == None:
            print("that node isn't there")
            return ([], [])
        queue.append(source)
        source.distance = 0
        while len(queue) > 0:
            curr = queue.pop(0)
            if curr == dest:
                break
            for edge in curr.edges:
                if edge[0].distance == 2729:
                    edge[0].distance = curr.distance + 1
                    queue.append(edge[0])
        nodes = []
        path = []
        if dest.distance == 2729:
            print("not connected")
            return None
        look = dest
        # infinite loop for some reason
        count = 0
        while look.name != source.name and count < 50:
            nodes.insert(0, look)
            for ed in look.edges:
                if ed[0].distance == look.distance - 1:
                    look = ed[0]
                    path.append(ed[1])
                    break
        nodes.insert(0, source)
        self.fix_distances()
        return path


    # changes all the distances back to the fake max value
    def fix_distances(self):
        for node in self.node_list:
            node.distance = 2729


    # gets the inverse of a string of moves
    def get_inverse(self, moves_string):
        # splits it into individual moves
        arr = moves_string.split(" ")
        # reverse the array
        arr.reverse()
        # take the opposite of each move that happens
        for i in range (len(arr)):
            if "'" in arr[i]:
                arr[i] = arr[i][0] # backwards to forwards
            else:
                arr[i] = arr[i] + "'" # forwards to backwards
        # return the joined together version
        return " ".join(arr)

    
    # prints the graph
    def print(self):
        for n in self.node_list:
            n.print()
