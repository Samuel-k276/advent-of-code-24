import os
from importlib import import_module

for i in range(1, 26):
   try:
      globals()[f'day_{i}'] = import_module(f'day_{i:02d}.day_{i}')
   except ImportError as e:
      print(f"Couldn't import day_{i}: {e}")

def count_subdirectories(path='.'):
   return len([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

for i in range(1, count_subdirectories()):
   if os.path.getsize(f"day_{i:02d}/input_{i}.txt") == 0:
      break
   
   print(f"Day {i}")
   print(f"Problem 1: {globals()[f'day_{i}'].problem_1()}")
   print(f"Problem 2: {globals()[f'day_{i}'].problem_2()}")
   print("---------------------")

print("Made by: @Samuel-k276")