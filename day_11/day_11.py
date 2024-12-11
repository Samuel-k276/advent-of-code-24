
def transform_stones(stones):
    new_stones = []
    for stone in stones:
        # Rule 1: If stone is 0, replace with 1
        if stone == 0:
            new_stones.append(1)
        # Rule 2: If number has even digits, split into two stones
        elif len(str(stone)) % 2 == 0:
            digits = str(stone)
            mid = len(digits) // 2
            left = int(digits[:mid])
            right = int(digits[mid:])
            new_stones.extend([left, right])
        # Rule 3: Multiply by 2024
        else:
            new_stones.append(stone * 2024)
    return new_stones

def solve_puzzle(initial_stones: dict, blinks):
   for i in range(blinks):
      new_stones = {}
      for stone in initial_stones:
         if stone == 0:
            if 1 in new_stones:
               new_stones[1] += initial_stones[stone]
            else:
               new_stones[1] = initial_stones[stone] 
         else:
            # calulate the number of digits
            digits = len(str(stone))
            if digits % 2 == 0:
               mid = digits // 2
               power = 10 ** mid
               left = stone // power
               right = stone % power
               if left in new_stones:
                  new_stones[left] += initial_stones[stone]
               else:
                  new_stones[left] = initial_stones[stone]
               if right in new_stones:
                  new_stones[right] += initial_stones[stone]
               else:
                  new_stones[right] = initial_stones[stone]
            else:
               new_stone = stone * 2024
               if new_stone in new_stones:
                  new_stones[new_stone] += initial_stones[stone]
               else:
                  new_stones[new_stone] = initial_stones[stone]
      initial_stones = new_stones

   return sum(initial_stones.values())

def parse_input(lines):
   test_stones = list(map(int, lines[0].split(' ')))
   input = {}
   for stone in test_stones:
      if stone in input:
         input[stone] += 1
      else:
         input[stone] = 1
   return input


def problem_1():
   with open('day_11/input_11.txt') as f:
      lines = f.readlines()
      input = parse_input(lines)
      result = solve_puzzle(input, 25)
   return result

def problem_2():
   with open('day_11/input_11.txt') as f:
      lines = f.readlines()
      input = parse_input(lines)
      result = solve_puzzle(input, 75)
   return result   