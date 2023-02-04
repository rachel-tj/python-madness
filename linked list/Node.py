class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    
    # prints the node
    def print(self):
        print(self.data)


    # prints the node and all sequential ones
    def printhash(self):
        temp = self
        while temp != None:
            print(str(temp.data), end = " ")
            temp = temp.next
        print()