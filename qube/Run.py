from QubeSolver import QubeSolver
import time


s = QubeSolver()


s.scramble()
t1 = time.time()
s.firstLayer()
s.secondLayer()
s.thirdLayer()
t2 = time.time()

print(t2 - t1)


s.show_top()
print()
s.show_left()
print()
s.show_back()
print()
s.show_right()
print()
s.show_front()
print()
s.show_bottom()


# left-right: back second row, all of top, all of bottom
# andy ashwin adam sidd 
# sid meyer zeeshan grant casey

# twenty runs:

# good: 15
# bad: 2
# exrra bad: 10