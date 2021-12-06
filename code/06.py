from collections import Counter
from pathlib import Path


def get_inp():
    return list(map(int, open(Path(__file__).parent.parent / "input" / "06.txt").readlines()[0].split(",")))


def process_day(current_fish, limit: int, current_day: int) -> int:
    if current_day == limit:
        return sum(current_fish.values())
    new_fish = {}
    for day, fish in current_fish.items():
        if day == 0:
            new_fish[8], new_fish[6] = fish, fish
        elif day == 7:
            new_fish[6] = fish if 6 not in new_fish else new_fish[6] + fish
        else:
            new_fish[day - 1] = fish
    return process_day(dict(sorted(new_fish.items())), limit, current_day + 1)


def part_one(lantern_fish: list[int]) -> int:
    return process_day(Counter(lantern_fish), 80, 0)


def part_two(lantern_fish: list[int]) -> int:
    return process_day(Counter(lantern_fish), 256, 0)


if __name__ == "__main__":
    inp = get_inp()
    print(f"Solution part one: {part_one(inp)} \nSolution part two: {part_two(inp)}")
