"""Solve https://adventofcode.com/2019/day/1"""
example = """12
14
1969
100756"""

def parse(input):
    return [int(n) for n in input.split()]

modules = parse(example)

with open('./data/DataDay01.txt') as file:
    input = file.read()

def get_fuel(mass):
    return mass//3-2

def solve_part1(data):
    """Get the sum of the fuel requirements."""
    modules = parse(data)
    tot = 0
    for module in modules:
        tot += get_fuel(module)
    return tot

if __name__ == '__main__':
    print(solve_part1(input))