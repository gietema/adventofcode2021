from typing import List


def get_depths() -> List[int]:
    with open("day_one.txt", "r") as f:
        return [int(line.rstrip()) for line in f.readlines()]


def part_one() -> int:
    depths = get_depths()
    return sum([depths[idx - 1] < depth for idx, depth in enumerate(depths)])


def part_two() -> int:
    depths = get_depths()
    return sum([sum(depths[idx-3:idx]) < sum(depths[idx-2:idx+1]) for idx in range(3, len(depths))])


if __name__ == "__main__":
    print(f"Solution part one: {part_one()} \nSolution part two: {part_two()}")
