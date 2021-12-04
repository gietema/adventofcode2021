from pathlib import Path


def get_input() -> list[int]:
    with open(str(Path(__file__).parent.parent / "input" / "01.txt")) as f:
        return [int(line.rstrip()) for line in f.readlines()]


def part_one(depths: list[int]) -> int:
    return sum([depths[idx - 1] < depth for idx, depth in enumerate(depths) if idx > 0])


def part_two(depths: list[int]) -> int:
    return sum([sum(depths[idx - 3 : idx]) < sum(depths[idx - 2 : idx + 1]) for idx in range(3, len(depths))])


if __name__ == "__main__":
    inp = get_input()
    print(f"Solution part one: {part_one(inp)} \nSolution part two: {part_two(inp)}")
