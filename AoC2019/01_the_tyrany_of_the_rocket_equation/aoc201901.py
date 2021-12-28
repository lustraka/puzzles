import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1"""
    return sum(mass // 3 - 2 for mass in data)

def get_fuel(mass):
    """Return complete fuel needed"""
    out = 0
    fuel = mass // 3 - 2
    while fuel > 0:
        out += fuel
        fuel = fuel // 3 - 2
    return out

def all_fuel(mass):
    """Calculate fuel while taking the mass of the fuel into account"""
    return 0 if (fuel := mass // 3 - 2) < 0 else fuel + all_fuel(fuel)

def part2(data):
    """Solve part 2"""
    return sum(all_fuel(mass) for mass in data)

def part2bis(data):
    """Solve part 2 without recurrsion with walrus operator"""
    total_fuel = 0
    for mass in data:
        while (mass := mass // 3 - 2) > 0:
            total_fuel += mass
    return total_fuel

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    solution3 = part2bis(data)

    return solution1, solution2, solution3

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))