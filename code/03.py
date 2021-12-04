import operator
import math
from pathlib import Path
from functools import partial


def get_input() -> list[str]:
    with open(str(Path(__file__).parent.parent / "input" / "03.txt")) as f:
        return [line.rstrip() for line in f.readlines()]


def part_one(binary_numbers: list[str]) -> int:
    epsilon, gamma, half_length = "", "", len(binary_numbers) // 2
    for idx in range(len(binary_numbers[0])):
        more_zeroes = [item[idx] for item in binary_numbers].count("0") > half_length
        gamma += str(int(more_zeroes))
        epsilon += str(int(not more_zeroes))
    return int(gamma, 2) * int(epsilon, 2)


def part_two(all_binary_numbers: list[str]) -> int:
    def keep_at_index(compare, binary_numbers: list[str], idx: int = 0):
        if len(binary_numbers) == 1:
            return int(binary_numbers[0], 2)
        to_keep = compare([i[idx] for i in binary_numbers].count("0"), len(binary_numbers) // 2)
        return keep_at_index(compare, [i for i in binary_numbers if i[idx] == str(int(to_keep))], idx + 1)

    return math.prod(map(partial(keep_at_index, binary_numbers=all_binary_numbers), [operator.le, operator.gt]))


if __name__ == "__main__":
    inp = get_input()
    print(f"Solution part one: {part_one(inp)} \nSolution part two: {part_two(inp)}")
