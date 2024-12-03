from day_1 import day_1
from day_2 import day_2
from day_3 import day_3


for i in range(1, 4):
   print(f"Day {i}")
   print(f"Problem 1: {globals()[f'day_{i}'].problem_1()}")
   print(f"Problem 2: {globals()[f'day_{i}'].problem_2()}")
   print("---------------------")