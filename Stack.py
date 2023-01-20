class Stack:

    def __init__(self):
        self.arr = []


    # adds an item to the top of the stack
    def push(self, num):
        self.arr.append(num)
    

    # removes the top of the stack
    def pop(self):
        return self.arr.pop()
    

    # returns if it's there
    def contains(self, num):
        return num in self.arr

    # returns the top item without removal
    def peek(self):
        return self.arr[len(self.arr)]
    
    def print(self):
        print(self.arr)