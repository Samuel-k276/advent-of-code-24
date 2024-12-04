def problem_1():
   with open('day_04/input_4.txt', 'r') as f:
      grid = [line.strip() for line in f.readlines()]
   f.close()

   def check_direction(x, y, dx, dy):
      for i in range(4):
         if not (0 <= x + i * dx < len(grid) and 0 <= y + i * dy < len(grid[0])):
            return False
         if grid[x + i * dx][y + i * dy] != "XMAS"[i]:
            return False
      return True

   directions = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]
   count = 0

   for x in range(len(grid)):
      for y in range(len(grid[0])):
         for dx, dy in directions:
            if check_direction(x, y, dx, dy):
               count += 1

   return count


def problem_2():
   def check_x_mas(x, y):
      return (((grid[x - 1][y - 1] == "M" and grid[x + 1][y + 1] == "S") or 
           (grid[x - 1][y - 1] == "S" and grid[x + 1][y + 1] == "M")) and
           ((grid[x - 1][y + 1] == "M" and grid[x + 1][y - 1] == "S") or 
           (grid[x - 1][y + 1] == "S" and grid[x + 1][y - 1] == "M")))

   with open('day_04/input_4.txt', 'r') as f:
      grid = [line.strip() for line in f.readlines()]
   f.close()

   count = 0

   for x in range(1, len(grid) - 1):
      for y in range(1, len(grid[0]) - 1):
         if grid[x][y] == "A":
            if check_x_mas(x, y):
               count += 1

   return count