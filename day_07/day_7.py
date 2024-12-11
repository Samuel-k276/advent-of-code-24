from itertools import product

def concatenate(a, b):
    """Concatenate two numbers."""
    return int(str(a) + str(b))

def evaluate_expression(numbers, operators):
    """Evaluate expression left to right with given numbers and operators."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        else:  # op == '||'
            result = concatenate(result, numbers[i + 1])
    return result

def can_make_value_1(test_value, numbers):
    """Check if test_value can be made with any combination of +, *, and || operators."""
    if len(numbers) == 1:
        return test_value == numbers[0]
    
    # Generate all possible combinations of operators
    operators = list(product(['+', '*'], repeat=len(numbers)-1))
    
    # Try each combination
    for ops in operators:
        if evaluate_expression(numbers, ops) == test_value:
            return True
    return False

def can_make_value_2(test_value, numbers):
    """Check if test_value can be made with any combination of +, *, and || operators."""
    if len(numbers) == 1:
        return test_value == numbers[0]
    
    # Generate all possible combinations of operators
    operators = list(product(['+', '*', '||'], repeat=len(numbers)-1))
    
    # Try each combination
    for ops in operators:
        if evaluate_expression(numbers, ops) == test_value:
            return True
    return False

def parse_line(line):
    """Parse a line into test value and numbers."""
    test_part, nums_part = line.strip().split(':')
    test_value = int(test_part)
    numbers = [int(x) for x in nums_part.split()]
    return test_value, numbers

def solve_calibration(input_text, problem):
    """Solve the calibration puzzle."""
    total = 0
    
    for line in input_text.strip().split('\n'):
        if not line:
            continue
        test_value, numbers = parse_line(line)
        if problem == 1:
            if can_make_value_1(test_value, numbers):
                total += test_value
        else: 
            if can_make_value_2(test_value, numbers):
                total += test_value
    
    return total


def problem_1():
    with open("day_07/input_7.txt") as f:
        data = f.read()
        result = solve_calibration(data, 1)
    return result

def problem_2():
    with open("day_07/input_7.txt") as f:
        data = f.read()
        result = solve_calibration(data, 2)
    return result

if __name__ == "__main__":
    print("Problem 1: {}".format(problem_1()))
    print("Problem 2: {}".format(problem_2()))