import copy
from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass
class Point:
    x: int
    y: int

    def fold(self, i: int, coord: str):
        if coord == "x" and i < self.x:
            self.x = i - (self.x - i)
        elif coord == "y" and i < self.y:
            self.y = i - (self.y - i)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def tolist(self) -> list[int, int]:
        return [self.x, self.y]


def get_input() -> tuple[list[Point], list[list[str | int]]]:
    inp = [
        Point(*[int(y) for y in x.rstrip().split(",")]) if "," in x else x.rstrip()
        for x in open(Path(__file__).parent.parent / "input" / "13.txt")
    ]
    coordinates = inp[: inp.index("")]
    folds_instruction = [
        [y.replace("fold along ", "") if "fold" in y else int(y) for y in x.split("=")]
        for x in inp[inp.index("") + 1 :]
    ]
    return coordinates, folds_instruction


def fold(coords: list[Point], folds: list[list[str | int]]) -> list[Point]:
    coords = copy.deepcopy(coords)
    for fold in folds:
        for coord in coords:
            coord.fold(fold[1], fold[0])
    return coords


def part_one(coords: list[Point], folds: list[list[str | int]]) -> int:
    return len(set(fold(coords, folds[:1])))


def part_two(coords: list[Point], folds: list[list[str | int]]):
    folded_coords = fold(coords, folds)
    c = np.array([c.tolist() for c in folded_coords])
    max_x, max_y = c[:, 0].max(), c[:, 1].max()
    field = np.zeros((max_y + 1, max_x + 1))
    for x in c:
        field[x[1], x[0]] = 1
    for line in field:
        print(" ".join(["#" if x == 1 else "." for x in line.astype(int).tolist()]))


if __name__ == "__main__":
    coordinates, folds_instructions = get_input()
    print(part_one(coordinates, folds_instructions[:1]))
    part_two(coordinates, folds_instructions)
