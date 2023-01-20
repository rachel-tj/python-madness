from Node import Node

class LinkedList:
    
    def __init__(self):
        self.head = None


    # adding something to the linked list
    def add(self, num):
        if self.head == None:
            self.head = Node(num)
            return;
        temp = self.head
        self.head = Node(num)
        self.head.next = temp
    

    # returns true if the linked list contains it
    def contains(self, data):
        temp = self.head
        while temp != None:
            if temp.data == data:
                return True
            temp = temp.next
        return False
    

    # removes something
    def remove(self, data):
        temp = self.head
        previous = None
        while temp != None:
            if temp.data == data:
                if previous == None:
                    self.head = temp.next
                else:
                    previous.next = temp.next
                return
            previous = temp
            temp = temp.next
    

    # prints the list
    def print(self):
        temp = self.head
        while temp != None:
            print(str(temp.data))
            temp = temp.next
