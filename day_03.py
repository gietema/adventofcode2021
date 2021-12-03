# Takeaway: collections.Counter's most_common()
import operator
import math
from functools import partial
from typing import List


def get_input():
    with open("day_03.txt", "r") as f:
        return [line.rstrip() for line in f.readlines()]


def part_one(binary_numbers: List[str]):
    epsilon, gamma, half_length = "", "", len(binary_numbers) // 2
    for idx in range(len(binary_numbers[0])):
        more_zeroes = [item[idx] for item in binary_numbers].count("0") > half_length
        gamma += str(int(more_zeroes))
        epsilon += str(int(not more_zeroes))
    return int(gamma, 2) * int(epsilon, 2)


def part_two(all_binary_numbers: List[str]):
    def keep_at_index(compare, binary_numbers: List[str], idx: int = 0):
        if len(binary_numbers) == 1:
            return int(binary_numbers[0], 2)
        to_keep = "1" if compare([i[idx] for i in binary_numbers].count("0"), len(binary_numbers) // 2) else "0"
        return keep_at_index(compare, [i for i in binary_numbers if i[idx] == to_keep], idx + 1)
    return math.prod(map(partial(keep_at_index, binary_numbers=all_binary_numbers), [operator.le, operator.gt]))


if __name__ == "__main__":
    inp = get_input()
    print(f"Solution part one: {part_one(inp)} \nSolution part two: {part_two(inp)}")
