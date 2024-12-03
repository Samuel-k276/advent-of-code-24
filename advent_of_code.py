from day_1 import sol_1
from day_2 import sol_2
from day_3 import sol_3


for i in range(1, 3):
   print(f"Day {i}")
   print(f"Problem 1: {globals()[f'sol_{i}'].problem_1()}")
   print(f"Problem 2: {globals()[f'sol_{i}'].problem_2()}")
   print("---------------------")