from Qube import Qube
from Graph import Graph

class QubeSolver:

    perfect_cube = Qube()

    def __init__(self):
        self.q = Qube()

    def makeGraph(self, mov):
        g = Graph()
        self.add_all_nodes(g)
        self.edge_helper(self.perfect_cube.top.side_arr, mov, g)
        self.edge_helper(self.perfect_cube.bottom.side_arr, mov, g)
        self.edge_helper(self.perfect_cube.front.side_arr, mov, g)
        self.edge_helper(self.perfect_cube.back.side_arr, mov, g)
        self.edge_helper(self.perfect_cube.left.side_arr, mov, g)
        self.edge_helper(self.perfect_cube.right.side_arr, mov, g)
        return g
    
    def firstLayer(self):
        self.makeDaisy()
        self.makeCorners()

    def makeDaisy(self):
        mov = ["U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'"]
        self.wheel(mov, "w01", "t01", None)
        
        mov = ["D", "D'", "L", "L'", "R", "R'", "F", "F'"]
        self.wheel(mov, "w10", "t10", None)

        mov = ["D", "D'", "R", "R'", "F", "F'", "L D L'", "L D' L'", "L' D' L", "L' D L"]
        self.wheel(mov, "w12", "t12", None)

        mov = ["D", "D'", "F", "F'", "L D L'", "L D' L'", "L' D' L", "L' D L", "R D R'", "R' D' R", "R D' R'", "R' D R"]
        self.wheel(mov, "w21", "t21", None)


    def makeCorners(self):
        mov = ["D", "D'", "R D R'", "R D' R'", "R' D R", "R' D' R", "L D L'", "L D' L'", "L' D L", "L' D' L", "F D F'", "F D' F'", "F' D F", "F' D' F", "B D B'", "B D' B'", "B' D B", "B' D' B"]
        self.wheel(mov, "w00", "t00", None)

        mov = ["D", "D'", "R D R'", "R D' R'", "R' D R", "R' D' R", "L D L'", "L D' L'", "F D F'", "F D' F'", "F' D F", "F' D' F", "B' D B", "B' D' B"]
        self.wheel(mov, "w02", "t02", None)

        mov = ["D", "D'", "R' D R", "R' D' R", "L D L'", "L D' L'", "F D F'", "F D' F'", "F' D F", "F' D' F"]
        self.wheel(mov, "w20", "t20", None)

        mov = ["D", "D'", "R' D R", "R' D' R", "F D F'", "F D' F'"]
        self.wheel(mov, "w22", "t22", None)
    
    def secondLayer(self):
        mov = ["D", "D'", "L D' L' D' F' D F", "R' D R D F D' F'", "F' D F D L D' L'", "B' D B D R D' R'", "F D' F' D' R' D R"]
        mov.append("R D' R' D' B' D B")
        mov.append("L' D L D B D' B'")
        mov.append("B D' B' D' L' D L")
        graph = self.makeGraph(mov)
        self.wheel(mov, "g10", "l10", graph)
        self.wheel(mov, "r10", "f10", graph)
        self.wheel(mov, "b10", "r10", graph)
        self.wheel(mov, "o10", "b10", graph)
    
    def plus_maker(self):
        answer = ""
        movString = "F D L D' L' F'"
        # this sometimes gets stuck in a loop
        while not self.plus():
            for i in range (4):
                if not self.lie() and not self.sit():
                    self.q.interpretCommand("D")
                    answer += "D "
                else:
                    break
            self.q.interpretCommands(movString)
            answer += movString + " "

    
    def yellow_face(self):
        movString = "L D L' D L D D L'"
        corners = self.count_corners()
        answer = ""
        while corners != 4:
            if corners == 0:
                while self.q.front.side_arr[2][0][0] == "y" or self.q.front.side_arr[2][2][0] == "y" or self.q.right.side_arr[2][0][0] != "y":
                    self.q.interpretCommand("D")
                    answer += "D "
            elif corners == 1:
                while self.q.bottom.side_arr[0][2][0] != "y":
                    self.q.interpretCommand("D")
                    answer += "D "
            elif corners == 2:
                while self.q.front.side_arr[2][2][0] != "y":
                    self.q.interpretCommand("D")
                    answer += "D "
            self.q.interpretCommands(movString)
            answer += movString + " "
            corners = self.count_corners()
    
    def bottom_corners(self):
        count = 0
        movString = "L' F L' B B L F' L' B B L L"
        if self.four_corn():
            return
        if self.q.back.side_arr[2][0][0] == self.q.back.side_arr[2][2][0]:
            self.q.interpretCommands(movString)
            self.bottom_corners()
        else:
            while self.q.back.side_arr[2][0][0] != self.q.back.side_arr[2][2][0] and count < 4:
                self.q.interpretCommand("D")
                count += 1
            if count == 4:
                self.q.interpretCommands(movString)
                count = 0
            self.bottom_corners()


    def final_step(self):
        count = 0
        movString = "F F D R L' F F R' L D F F"
        if self.bottom_layer():
            self.twisttie()
            return
        if self.q.back.side_arr[2][0][0] == self.q.back.side_arr[2][1][0]:
            self.q.interpretCommands(movString)
            self.final_step()
        else:
            while self.q.back.side_arr[2][0][0] != self.q.back.side_arr[2][1][0] and count < 4:
                self.q.interpretCommand("D")
                count += 1
            if count == 4:
                self.q.interpretCommands(movString)
                count = 0
            self.final_step()
    
    def twisttie(self):
        arr = self.q.front.side_arr
        while arr[1][0][0] != arr[2][0][0]:
            self.q.interpretCommand("D")



    def thirdLayer(self):
        self.plus_maker()
        self.yellow_face()
        self.bottom_corners()
        self.final_step()





    def wheel(self, mov, start, end, g):
        if g == None:
            graph = self.makeGraph(mov)
        else:
            graph = g
        a = self.q.find_element(start)
        ax = graph.shortest_path(a, end)
        if ax == None:
            return
        self.q.interpretCommands(ax)

    

    def edge_helper(self, arr, moves_list, g):
        for line in arr:
            for el in line:
                for mov in moves_list:
                    old_val = self.perfect_cube.color_to_place(el)
                    self.perfect_cube.interpretCommands(mov)
                    new_val = self.perfect_cube.find_element(el)
                    g.add_edge(old_val, new_val, mov)

                   

                    inv = self.perfect_cube.get_inverse(mov)
                    self.perfect_cube.interpretCommands(inv)
    

    def add_nodes(self, let, g):
        for i in range (3):
            for j in range (3):
                val = let + str(i) + str(j)
                g.add_node(val)
    
    def lie(self):
        arr = self.q.bottom.side_arr
        if arr[1][0][0] == "y" and arr[1][2][0] == "y":
            return True
        return False
    
    def sit(self):
        arr = self.q.bottom.side_arr
        if arr[1][2][0] == "y" and arr[2][1][0] == "y":
            return True
        return False
    
    def plus(self):
        arr = self.q.bottom.side_arr
        if arr[1][0][0] == "y" and arr[2][1][0] == "y" and arr[0][1][0] == "y" and arr[2][1][0] == "y":
            return True
        return False
    
    def count_corners(self):
        arr = self.q.bottom.side_arr
        count = 0
        for i in range (0, 3, 2):
            for j in range (0, 3, 2):
                if arr[i][j][0] == "y":
                    count += 1
        return count

    def bottom_layer(self):
        front = self.q.front.side_arr
        back = self.q.back.side_arr
        right = self.q.right.side_arr
        left = self.q.left.side_arr
        leutner = [False] * 4
        if front[2][0][0] == front[2][1][0] and front[2][1][0] == front[2][2][0]:
            leutner[0] = True
        if back[2][0][0] == back[2][1][0] and back[2][1][0] == back[2][2][0]:
            leutner[1] = True
        if right[2][0][0] == right[2][1][0] and right[2][1][0] == right[2][2][0]:
            leutner[2] = True
        if left[2][0][0] == left[2][1][0] and left[2][1][0] == left[2][2][0]:
            leutner[3] = True
        return leutner[0] and leutner[1] and leutner[2] and leutner[3]

    def four_corn(self):
        front = self.q.front.side_arr
        back = self.q.back.side_arr
        right = self.q.right.side_arr
        left = self.q.left.side_arr
        leutner = [False] * 4
        if front[2][0][0] == front[2][2][0]:
            leutner[0] = True
        if back[2][0][0] == back[2][2][0]:
            leutner[1] = True
        if right[2][0][0] == right[2][2][0]:
            leutner[2] = True
        if left[2][0][0] == left[2][2][0]:
            leutner[3] = True
        return leutner[0] and leutner[1] and leutner[2] and leutner[3]

    


    
    def add_all_nodes(self, g):
        self.add_nodes("f", g)
        self.add_nodes("b", g)
        self.add_nodes("t", g)
        self.add_nodes("d", g)
        self.add_nodes("l", g)
        self.add_nodes("r", g)
    
    def show_front(self):
        self.q.front.print()
    
    def show_back(self):
        self.q.back.print()
    
    def show_right(self):
        self.q.right.print()
    
    def show_left(self):
        self.q.left.print()
    
    def show_top(self):
        self.q.top.print()
    
    def show_bottom(self):
        self.q.bottom.print()

    def scramble(self):
        self.q.scramble()