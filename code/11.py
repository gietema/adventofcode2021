import copy
from itertools import chain, combinations
from pathlib import Path


def get_adjacent(idx_line, idx):
    return [
        (new_y, new_x)
        for x, y in set(combinations([-1, -1, 0, 1, 1, 0, -1], 2))
        if 0 <= (new_y := (idx_line + y)) < 10 and 0 <= (new_x := (idx + x)) < 10 and not (x == 0 and y == 0)
    ]


def increase_energy_level(octopuses: list[list[int]]) -> list[list[int]]:
    for idx_line, line in enumerate(octopuses):
        for idx, o in enumerate(line):
            octopuses[idx_line][idx] += 1
    return octopuses


def solve(octopuses: list[list[int]], part_one: bool = False) -> int:
    octopuses = copy.deepcopy(octopuses)
    num_flashes, steps = 0, 0
    while not all([octopus == 0 for octopus in chain(*octopuses)]):
        steps += 1
        flashed_octopuses = []
        octopuses = increase_energy_level(octopuses)
        while any([o > 9 for o in chain(*octopuses)]):
            for idx_line, line in enumerate(octopuses):
                for idx, o in enumerate(line):
                    if o > 9 and (idx_line, idx) not in flashed_octopuses:
                        for adjacent in get_adjacent(idx_line, idx):
                            if adjacent not in flashed_octopuses:
                                octopuses[adjacent[0]][adjacent[1]] += 1
                        octopuses[idx_line][idx] = 0
                        flashed_octopuses.append((idx_line, idx))
        num_flashes += len(flashed_octopuses)
        if part_one and steps == 100:
            return num_flashes
    return steps


if __name__ == "__main__":
    inp = [[int(octo) for octo in line.rstrip()] for line in open(Path(__file__).parent.parent / "input" / "11.txt")]
    print(f"Solution part one: {solve(inp, True)} \nSolution part two: {solve(inp)}")
