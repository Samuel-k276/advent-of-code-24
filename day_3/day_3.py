import re

def problem_1():
   with open('day_3/input_3.txt', 'r') as f:
      data = f.read()
      pattern = re.compile(r'mul\((\d+),(\d+)\)')
      matches = pattern.findall(data)
      result = sum(int(x) * int(y) for x, y in matches)
   f.close()
   return result

def problem_2():
   with open('day_3/input_3.txt', 'r') as f:
      data = f.read()
      pattern = re.compile(r'mul\((\d+),(\d+)\)')
      start = 0
      end = 0
      result = 0

      while True:
         if data[start:].find("don't()") == -1:
            result += sum(int(x) * int(y) for x, y in pattern.findall(data[start:]))
            break
         else:
            end = data.find("don't()", start)
            result += sum(int(x) * int(y) for x, y in pattern.findall(data[start:end]))
         
         start = end
         if data.find("do()", start) == -1:
            break
         else:
            start = data.find("do()", start)
   f.close()
   return result