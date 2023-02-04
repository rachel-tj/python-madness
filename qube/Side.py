import numpy as np

class Side:


    def __init__(self, color):
        self.side_arr = [0] * 3
        # traverse through the rows
        for i in range (len(self.side_arr)):
            self.side_arr[i] = [0] * 3
            # add a color id such as "g12" for green row 1 column 2
            for j in range (3):
                self.side_arr[i][j] = color + str(i) + str(j)


    # prints the side array
    def print(self):
        # traverse through rows
        for row in self.side_arr:
            print("[", end="")
            # traverse through elements
            for el in row:
                print(el[0], end=" ")
            print("]")

