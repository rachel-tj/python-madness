from Side import Side
import random

class Qube:

    def __init__(self):
        self.front = Side("r")
        self.left = Side("g")
        self.right = Side("b")
        self.top = Side("w")
        self.bottom = Side("y")
        self.back = Side("o")
    
    def U(self):
        self.frontHelper(0)
        self.clockwise(self.top.side_arr)
    
    def D(self):
        self.frontRHelper(2)
        self.clockwise(self.bottom.side_arr)

    def Ui(self):
        self.frontRHelper(0)
        self.counter_clockwise(self.top.side_arr)

    def Di(self):
        self.frontHelper(2)
        self.counter_clockwise(self.bottom.side_arr)

    def L(self):
        self.leftHelper(0)
        self.clockwise(self.left.side_arr)
    
    def R(self):
        self.leftRHelper(2)
        self.clockwise(self.right.side_arr)
    
    def Li(self):
        self.leftRHelper(0)
        self.counter_clockwise(self.left.side_arr)
    
    # SWITCH CLOCKWISE
    def Ri(self):
        self.leftHelper(2)
        self.counter_clockwise(self.right.side_arr)
    
    def F(self):
        self.planeHelper(2)
        self.clockwise(self.front.side_arr)
    
    def B(self):
        self.planeRHelper(0)
        self.clockwise(self.back.side_arr)
    
    def Fi(self):
        self.planeRHelper(2)
        self.counter_clockwise(self.front.side_arr)
    
    def Bi(self):
        self.planeHelper(0)
        self.counter_clockwise(self.back.side_arr)

    def frontHelper(self, num):
        a = tuple(self.left.side_arr[num])
        b = tuple(self.back.side_arr[num])
        c = tuple(self.right.side_arr[num])
        d = tuple(self.front.side_arr[num])
        self.front.side_arr[num] = list(c)
        self.left.side_arr[num] = list(d)
        self.back.side_arr[num] = list(a)
        self.right.side_arr[num] = list(b)

    def frontRHelper(self, num):
        a = tuple(self.left.side_arr[num])
        b = tuple(self.back.side_arr[num])
        c = tuple(self.right.side_arr[num])
        d = tuple(self.front.side_arr[num])
        self.front.side_arr[num] = list(a)
        self.left.side_arr[num] = list(b)
        self.back.side_arr[num] = list(c)
        self.right.side_arr[num] = list(d)


    def leftHelper(self, num):
        other = [2, 0][num == 2]
        a = self.toTup(self.top.side_arr)
        b = self.toTup(self.front.side_arr)
        c = self.toTup(self.bottom.side_arr)
        d = self.toTup(self.back.side_arr)
        for i in range (3):
            self.front.side_arr[i][num] = a[i][num]
            self.bottom.side_arr[i][num] = b[i][num]
            self.back.side_arr[2 - i][other] = c[i][num]
            self.top.side_arr[i][num] = d[2 - i][other]

    
    def leftRHelper(self, num):
        other = [2, 0][num == 2]
        a = self.toTup(self.top.side_arr)
        b = self.toTup(self.front.side_arr)
        c = self.toTup(self.bottom.side_arr)
        d = self.toTup(self.back.side_arr)
        for i in range (3):
            self.front.side_arr[i][num] = c[i][num]
            self.bottom.side_arr[i][num] = d[2 - i][other]
            self.back.side_arr[2 - i][other] = a[i][num]
            self.top.side_arr[i][num] = b[i][num]
        
    def planeHelper(self, num):
        other = [2, 0][num == 2]
        a = self.toTup(self.top.side_arr)
        b = self.toTup(self.left.side_arr)
        c = self.toTup(self.bottom.side_arr)
        d = self.toTup(self.right.side_arr)
        for i in range (3):
            self.right.side_arr[i][other] = a[num][i]
            self.bottom.side_arr[other][2 - i] = d[i][other]
            self.left.side_arr[i][num] = c[other][i]
            self.top.side_arr[num][2 - i] = b[i][num]

    def planeRHelper(self, num):
        other = [2, 0][num == 2]
        a = self.toTup(self.top.side_arr)
        b = self.toTup(self.left.side_arr)
        c = self.toTup(self.bottom.side_arr)
        d = self.toTup(self.right.side_arr)
        for i in range (3):
            self.right.side_arr[2 - i][other] = c[other][i]
            self.bottom.side_arr[other][i] = b[i][num]
            self.left.side_arr[2 - i][num] = a[num][i]
            self.top.side_arr[num][i] = d[i][other]
        
    def clockwise(self, side_piece):
        a = self.toTup(side_piece)
        for i in range (3):
            for j in range (3):
                side_piece[j][i] = a[2 - i][j]
        
    def counter_clockwise(self, side_piece):
        a = self.toTup(side_piece)
        for i in range (3):
            for j in range (3):
                side_piece[j][i] = a[i][2 - j]

    def randomMove(self, num):
        if num == 0:
            self.U()
        elif num == 1:
            self.Ui()
        elif num == 2:
            self.D()
        elif num == 3:
            self.Di()
        elif num == 4:
            self.L()
        elif num == 5:
            self.Li()
        elif num == 6:
            self.R()
        elif num == 7:
            self.Ri()
        elif num == 8:
            self.F()
        elif num == 9:
            self.Fi()
        elif num == 10:
            self.B()
        elif num == 11:
            self.Bi()
        
    def num_to_move(self, num):
        arr = ["U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'"]
        return arr[num]
    
    def get_inverse(self, moves_string):
        arr = moves_string.split(" ")
        arr.reverse()
        for i in range (len(arr)):
            if "'" in arr[i]:
                arr[i] = arr[i][0]
            else:
                arr[i] = arr[i] + "'"
        return " ".join(arr)
        
    def scramble(self):
        for i in range (20):
            num = random.randint(0, 11)
            self.randomMove(num)
    
    def starting(self):
        self.leftTurn()
        self.leftTurn()
        self.rightTurn()
        self.rightTurn()
        self.frontTurn()
        self.frontTurn()
        self.backTurn()
        self.backTurn()
    
    def interpretCommand(self, com):
        com = com.replace("'", "i")
        com = "self." + com + "()"
        try:
            exec(com)
        except:
            return

    def interpretCommands(self, com):
        arr = com.split(" ")

        for c in arr:
            self.interpretCommand(c)

    def place_to_color(self, el):
        place = el[0]
        i = el[1]
        j = el[2]
        if place == "f":
            return self.front.side_arr[i][j]
        elif place == "b":
            return self.back.side_arr[i][j]
        elif place == "t":
            return self.top.side_arr[i][j]
        elif place == "d":
            return self.bottom.side_arr[i][j]
        elif place == "l":
            return self.left.side_arr[i][j]
        elif place == "r":
            return self.right.side_arr[i][j]
        
    def color_to_place(self, el):
        color = el[0]
        color_string = "rogbwy"
        place_string = "fblrtd"
        index = color_string.index(color)
        return place_string[index] + el[1:]

    def find_element_helper(self, el, side, let):
        arr = side.side_arr
        for i in range (3):
            for j in range (3):
                if arr[i][j] == el:
                    return let + str(i) + str(j)
        
    def find_element(self, el):
        a = [self.find_element_helper(el, self.front, "f"), self.find_element_helper(el, self.back, "b"), self.find_element_helper(el, self.top, "t"), self.find_element_helper(el, self.bottom, "d"), self.find_element_helper(el, self.left, "l"), self.find_element_helper(el, self.right, "r")]
        for thing in a:
            if thing != None:
                return thing


            
    def toTup(self, arr):
        return tuple(map(tuple, arr))

    def print(self):
        print(self.left.print())