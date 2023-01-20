class Queue:

    def __init__(self):
        self.arr = []
    
    
    # adds something to the queue
    def add(self, num):
        self.arr.append(num)


    # removes the first item and returns it
    def pop(self):
        temp = self.arr[0]
        self.arr.remove(temp)
        return temp

    # only returns the first item without removal
    def pop(self):
        temp = self.arr[0]
        return temp
    

    # returns true if it's there
    def contains(self, num):
        return num in self.arr
    
    # prints the queue
    def print(self):
        print(self.arr)