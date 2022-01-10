# Advent of Code 2019
[AoC 2019](https://adventofcode.com/2019) | [RealPython: AoC Tutorial](https://realpython.com/python-advent-of-code/#practicing-advent-of-code-day-1-2019) |

## Contents
- [Day 1: The Tyrany of the Rocket Equation](01_the_tyrany_of_the_rocket_equation)
	- ⭐ Part I uses an integer division `//` and a generator (comprehension).
	- ⭐ Part II solved with and without recurrsion. Also uses the waldrus opertor (available in Python 3.8 and later)
- [Day 2: 1202 Program Alarm](02_1202_program_alarm)
	- ⭐ Part I finds a value at position 0 after running an Intcode program.
	- ⭐ Part II finds `noun and verb` values that cause the Intcode program to produce the required output.
- [Day 3 : Crossed Wires](03_crossed_wires/aoc201903.ipynb)
    - ⭐ Part I solved using a numpy matrix.
    - Part II needs some tree search algorithm.
- [Day 4: Secure Container](04_secure_container/aoc201904.ipynb)
	- ⭐ Part I uses type conversions, `collection.Counter()`, and set operation (intersection).
	- ⭐ Part II solved with a minor adjustement of an algorithm for part I.
- [Day 5: Sunny wit a Chance of Asteroids](05_sunny_asteroids//oac201905.ipynb)
	- Part I
	- Part II
- [Day 6: ]()
	- Part I
	- Part II
- [Day 7: ]()
	- Part I
	- Part II
- [Day 8: ]()
	- Part I
	- Part II
- [Day 9: ]()
	- Part I
	- Part II
- [Day 10: ]()
	- Part I
	- Part II
- [Day 11: ]()
	- Part I
	- Part II
- [Day 12: ]()
	- Part I
	- Part II
- [Day 13: ]()
	- Part I
	- Part II
- [Day 14: ]()
	- Part I
	- Part II
- [Day 15: ]()
	- Part I
	- Part II
- [Day 16: ]()
	- Part I
	- Part II
- [Day 17: ]()
	- Part I
	- Part II
- [Day 18: ]()
	- Part I
	- Part II
- [Day 19: ]()
	- Part I
	- Part II
- [Day 20: ]()
	- Part I
	- Part II
- [Day 21: ]()
	- Part I
	- Part II
- [Day 22: ]()
	- Part I
	- Part II
- [Day 23: ]()
	- Part I
	- Part II
- [Day 24: ]()
	- Part I
	- Part II
- [Day 25: ]()
	- Part I
	- Part II


## A Starting Template
```python
import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""

def part1(data):
    """Solve part 1"""

def part2(data):
    """Solve part 2"""

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
```

## A Template Using `pytest`
```python
# test_aoc_template.py

import pathlib
import pytest
import aoc_template as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == ...

@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == ...
```
