from itertools import chain
from math import prod
from pathlib import Path


def get_heightmap():
    heightmap = [[int(p) for p in line.rstrip()] for line in open(Path(__file__).parent.parent / "input" / "09.txt")]
    # add padding to simplify indexing
    heightmap = [[10] + line + [10] for line in heightmap]
    return [[10] * len(heightmap[0])] + heightmap + [[10] * len(heightmap[0])]


def is_low_point(heightmap, point, line_idx, idx):
    return all([point < heightmap[p[0]][p[1]] for p in points_to_explore(line_idx, idx)])


def points_to_explore(line_idx, idx):
    return [(line_idx + 1, idx), (line_idx - 1, idx), (line_idx, idx + 1), (line_idx, idx - 1)]


def part_one(heightmap):
    low_points = [
        [1 + point for idx, point in enumerate(line[1:-1], 1) if is_low_point(heightmap, point, line_idx, idx)]
        for line_idx, line in enumerate(heightmap[1:-1], 1)
    ]
    return sum([*chain(*[p for p in low_points if len(p) > 0])])


def part_two(heightmap):
    basins = []
    for line_idx, line in enumerate(heightmap[1:-1], 1):
        for idx, point in enumerate(line[1:-1], 1):
            if is_low_point(heightmap, point, line_idx, idx):
                basins.append([heightmap[p[0]][p[1]] for p in get_basin_points(heightmap, idx, line_idx)])
    return prod(sorted([len(i) for i in basins])[-3:])


def get_basin_points(heightmap, idx, line_idx):
    basin_points = [(line_idx, idx)]
    to_explore = points_to_explore(line_idx, idx)
    while len(to_explore) > 0:
        if (p := to_explore.pop()) not in basin_points and heightmap[p[0]][p[1]] < 9:
            to_explore.extend(points_to_explore(p[0], p[1]))
            basin_points.append(p)
    return basin_points


if __name__ == "__main__":
    inp = get_heightmap()
    print(f"Solution part one: {part_one(inp)} \nSolution part two: {part_two(inp)}")
