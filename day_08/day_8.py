
def parse_grid(input_str):
    return [list(line) for line in input_str.splitlines()]

def get_antennas(grid):
    antennas = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                if grid[i][j] not in antennas:
                    antennas[grid[i][j]] = []
                antennas[grid[i][j]].append((j, i))
    return antennas

def solve(input_str, repetition):
    grid = parse_grid(input_str)
    antennas = get_antennas(grid)
    rows = len(grid)
    cols = len(grid[0])
    
    # Find all antinodes
    antinodes = set()
    
    # For each type of antenna
    for freq in antennas:
        coords = antennas[freq]
        # For each pair of antennas of same type
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                if repetition == 1:
                    antinodes.add(coords[i])
                    antinodes.add(coords[j])
                x1, y1 = coords[i] # First antenna
                x2, y2 = coords[j] # Second antenna
            
                p1 = (x1 - (x2 - x1), y1 - (y2 - y1))
                p1 = (int(p1[0]), int(p1[1]))
                p2 = (x2 + x2 - x1, y2 + y2 - y1)
                p2 = (int(p2[0]), int(p2[1]))

                # If repetition is 0, we only need to add the two first antinodes
                if repetition == 0:
                    if 0 <= p1[0] < cols and 0 <= p1[1] < rows:
                        antinodes.add(p1)
                    if 0 <= p2[0] < cols and 0 <= p2[1] < rows:
                        antinodes.add(p2)
                    continue

                while 0 <= p1[0] < cols and 0 <= p1[1] < rows:
                    antinodes.add(p1)
                    p1 = (int(p1[0]), int(p1[1]))
                    p1 = (p1[0] - (x2 - x1), p1[1] - (y2 - y1))

                while 0 <= p2[0] < cols and 0 <= p2[1] < rows:
                    antinodes.add(p2)
                    p2 = (p2[0] + x2 - x1, p2[1] + y2 - y1)
                    p2 = (int(p2[0]), int(p2[1]))
                
    return len(antinodes)

def problem_1():
    with open("day_08/input_8.txt") as f:
        data = f.read()
        result = solve(data, 0)
    return result

def problem_2():
    with open("day_08/input_8.txt") as f:
        data = f.read()
        result = solve(data, 1)
    return result
