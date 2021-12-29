import pathlib
import pytest
import aoc201902 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example():
    return aoc.parse('example.txt')

@pytest.fixture
def input():
    return aoc.parse('input.txt', 12, 2)

def test_parse_example1(example):
    """Test that input is parsed properly"""
    assert example == [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

def test_part1_example(example):
    """Test part 1 on example input"""
    assert aoc.part1(example) == 3500

def test_part1_input(input):
    """Test part 2 on example input"""
    assert aoc.part1(input) == 3409710