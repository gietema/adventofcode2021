from itertools import chain

from dataclasses import dataclass
from collections import Counter
from pathlib import Path


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Line:
    top_left: Point
    bottom_right: Point

    @property
    def y_range(self):
        if self.top_left.y > self.bottom_right.y:
            return range(self.top_left.y, self.bottom_right.y - 1, -1)
        return range(self.top_left.y, self.bottom_right.y + 1)

    @property
    def x_range(self):
        if self.top_left.x > self.bottom_right.x:
            return range(self.top_left.x, self.bottom_right.x - 1, -1)
        return range(self.top_left.x, self.bottom_right.x + 1)

    def is_horizontal(self) -> bool:
        return self.top_left.y == self.bottom_right.y

    def is_vertical(self) -> bool:
        return self.top_left.x == self.bottom_right.x

    def covers(self) -> list[Point]:
        if self.is_horizontal():
            return [Point(x, self.top_left.y) for x in self.x_range]
        if self.is_vertical():
            return [Point(self.top_left.x, y) for y in self.y_range]
        # line is diagonal
        return [Point(x, y) for x, y in zip(self.x_range, self.y_range)]


def get_lines() -> list[Line]:
    return [(Line(*[Point(*[int(coord) for coord in point.split(",")])
                    for point in input_line.rstrip().split("->")]))
            for input_line in open(Path(__file__).parent.parent / "input" / "05.txt")]


def part_one(lines: list[Line]) -> int:
    counter = Counter(chain(*[line.covers() for line in lines if line.is_vertical() or line.is_horizontal()]))
    return len([point for point, count in counter.items() if count >= 2])


def part_two(lines: list[Line]) -> int:
    counter = Counter(chain(*[line.covers() for line in lines]))
    return len([point for point, count in counter.items() if count >= 2])


if __name__ == "__main__":
    lines = get_lines()
    print(f"Solution part one: {part_one(lines)} \nSolution part two: {part_two(lines)}")
