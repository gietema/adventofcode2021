import math
from pathlib import Path


def get_input():
    return sorted([int(i) for i in open(Path(__file__).parent.parent / "input" / "07.txt").readlines()[0].split(",")])


def brute_force_answer(positions: list[int], triangular_number: bool = False):
    max_change = math.inf
    for i in range(min(positions), max(positions)):
        max_change_current = 0
        for position in positions:
            change = abs(i - position)
            max_change_current += change * (change + 1) // 2 if triangular_number else change
        if max_change > max_change_current:
            max_change = max_change_current
    return max_change


def part_one(positions: list[int]) -> int:
    return brute_force_answer(positions)


def part_two(positions: list[int]) -> int:
    return brute_force_answer(positions, triangular_number=True)


if __name__ == "__main__":
    inp = get_input()
    print(f"Solution part one: {part_one(inp)} \nSolution part two: {part_two(inp)}")
