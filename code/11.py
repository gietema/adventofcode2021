import copy
from itertools import chain, combinations
from pathlib import Path


def get_adjacent(y, x):
    return [
        (new_y, new_x)
        for i, j in set(combinations([-1, -1, 0, 1, 1, 0, -1], 2))
        if 0 <= (new_y := (y + j)) < 10 and 0 <= (new_x := (x + i)) < 10 and not (i == 0 and j == 0)
    ]


def increase_energy_level(octopuses: list[list[int]]) -> list[list[int]]:
    for idx_line, line in enumerate(octopuses):
        for idx, o in enumerate(line):
            octopuses[idx_line][idx] += 1
    return octopuses


def should_flash(octopuses):
    return any([o > 9 for o in chain(*octopuses)])


def all_flashed(octopuses):
    return all([octopus == 0 for octopus in chain(*octopuses)])


def solve(octopuses: list[list[int]], part_one: bool = False) -> int:
    octopuses, num_flashes, steps = copy.deepcopy(octopuses), 0, 0
    while not all_flashed(octopuses):
        steps, octopuses, flashed_octopuses = steps + 1, increase_energy_level(octopuses), []
        while should_flash(octopuses):
            octopuses, flashed_octopuses = flash(octopuses, flashed_octopuses)
        num_flashes += len(flashed_octopuses)
        if part_one and steps == 100:
            return num_flashes
    return steps


def flash(octopuses, flashed_octopuses):
    for idx_line, line in enumerate(octopuses):
        for idx, o in filter(lambda x: x[1] > 9 and (idx_line, x[0]) not in flashed_octopuses, enumerate(line)):
            for adjacent in filter(lambda x: x not in flashed_octopuses, get_adjacent(idx_line, idx)):
                octopuses[adjacent[0]][adjacent[1]] += 1
            octopuses[idx_line][idx] = 0
            flashed_octopuses.append((idx_line, idx))
    return octopuses, flashed_octopuses


if __name__ == "__main__":
    inp = [[int(octo) for octo in line.rstrip()] for line in open(Path(__file__).parent.parent / "input" / "11.txt")]
    print(f"Solution part one: {solve(inp, True)} \nSolution part two: {solve(inp)}")
