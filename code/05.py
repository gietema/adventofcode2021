from collections import Counter
from dataclasses import dataclass
from itertools import chain
from pathlib import Path


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Line:
    start: Point
    end: Point

    @property
    def y_range(self):
        if self.start.y > self.end.y:
            return range(self.start.y, self.end.y - 1, -1)
        return range(self.start.y, self.end.y + 1)

    @property
    def x_range(self):
        if self.start.x > self.end.x:
            return range(self.start.x, self.end.x - 1, -1)
        return range(self.start.x, self.end.x + 1)

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def covers(self) -> list[Point]:
        if self.is_horizontal():
            return [Point(x, self.start.y) for x in self.x_range]
        if self.is_vertical():
            return [Point(self.start.x, y) for y in self.y_range]
        # line is diagonal
        return [Point(x, y) for x, y in zip(self.x_range, self.y_range)]


def get_lines() -> list[Line]:
    return [
        Line(*[Point(*[int(coord) for coord in point.split(",")]) for point in input_line.rstrip().split("->")])
        for input_line in open(Path(__file__).parent.parent / "input" / "05.txt")
    ]


def part_one(lines: list[Line]) -> int:
    counter = Counter(chain(*[line.covers() for line in lines if line.is_vertical() or line.is_horizontal()]))
    return len([point for point, count in counter.items() if count >= 2])


def part_two(lines: list[Line]) -> int:
    counter = Counter(chain(*[line.covers() for line in lines]))
    return len([point for point, count in counter.items() if count >= 2])


if __name__ == "__main__":
    inp = get_lines()
    print(f"Solution part one: {part_one(inp)} \nSolution part two: {part_two(inp)}")
