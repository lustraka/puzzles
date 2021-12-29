import pathlib

def parse(input, noun=9, verb=10):
    """Parse input"""
    puzzle_input = pathlib.Path(input).read_text().strip()
    data = [int(n) for n in puzzle_input.split(',')]
    data[1], data[2] = noun, verb
    return data

def part1(intcodeprg):
    """Solve part 1"""
    
    # Initialize address
    address = 0
    while address < len(intcodeprg):
        opcode = intcodeprg[address]
        if opcode == 99:
            return intcodeprg[0]
        elif opcode in [1, 2]:
            op1 = intcodeprg[intcodeprg[address + 1]]
            op2 = intcodeprg[intcodeprg[address + 2]]
            dest = intcodeprg[address + 3]
            intcodeprg[dest] = op1 + op2 if opcode == 1 else op1 * op2
            address += 4
        else:
            print(f"Unknown opcode '{opcode}")
            break
    return -1

def part2(data):
    """Solve part 2"""
    for noun in range(100):
        for verb in range(100):
            intcodeprg = data.copy()
            intcodeprg[1], intcodeprg[2] = noun, verb
            output = part1(intcodeprg)
            if output == 19690720:
                return noun * 100 + verb
    return -1
