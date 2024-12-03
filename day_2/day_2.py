def is_safe(report):
   increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report)-1))
   decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report)-1))
   return increasing or decreasing

def problem_1():
   with open('day_2/input_2.txt', 'r') as f:
      safe_count = 0
      for line in f.readlines():
         levels = list(map(int, line.split()))
         if is_safe(levels):
            safe_count += 1
   return safe_count

def is_safe_with_dampener(report):
   if is_safe(report):
      return True
   for i in range(len(report)):
      if is_safe(report[:i] + report[i+1:]):
         return True
   return False

def problem_2():
   with open('day_2/input_2.txt', 'r') as f:
      safe_count = 0
      for line in f.readlines():
         levels = list(map(int, line.split()))
         if is_safe_with_dampener(levels):
            safe_count += 1
   return safe_count