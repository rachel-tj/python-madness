from Node import Node

class HashMap:

    def __init__(self):
        self.size = 6
        self.arr = [None] * self.size
        self.load = 0.7
    

    # adds something to the hashmap
    def helper(self, node):
        place = self.func(node.data)
        if self.arr[place] != None:
            temp = self.arr[place]
            while temp.next != None:
                temp = temp.next
            temp.next = node
        else:
            self.arr[place] = node
        if (self.calc_load() > self.load):
            self.size *= 2
            self.rehash()
    

    # the main add method
    def add(self, data):
        node = Node(data)
        self.helper(node)
    
    
    # the hash function
    def func(self, data):
        sum = 0
        for letter in data:
            sum += ord(letter)
        return sum % self.size

    
    #returns true if it's in there
    def contains(self, key):
        place = self.func(key)
        temp = self.arr[place]
        while temp != None:
            if temp.data == key:
                return True
            temp = temp.next
        return False


    # removes an item
    def remove(self, key):
        place = self.func(key)
        temp = self.arr[place]
        previous = None
        while temp != None:
            if temp.data == key:
                if previous == None:
                    self.arr[place] = temp.next
                else:
                    previous.next = temp.next
            previous = temp
            temp = temp.next

    
    # calculates the load factor
    def calc_load(self):
        count = 0;
        for item in self.arr:
            if item != None:
                count += 1
        return count / len(self.arr)


    # rehashes the hashmap when the load factor is too large
    def rehash(self):
        old = self.arr
        self.arr = [None] * self.size
        for item in old:
            if item == None:
                continue
            self.recur(item)


    # uses recursion to help rehash
    def recur(self, node):
        if node.next == None:
            self.helper(node)
        else:
            self.recur(node.next)
            node.next = None
            self.helper(node)
    

    # prints the hashmap
    def print(self):
        for i in range (len(self.arr)):
            item = self.arr[i]
            print(str(i), end = " ")
            if item == None:
                print()
                continue;
            item.printhash()
