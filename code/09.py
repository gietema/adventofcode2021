from math import prod
from pathlib import Path


def get_heightmap():
    heightmap = [[int(p) for p in line.rstrip()] for line in open(Path(__file__).parent.parent / "input" / "09.txt")]
    # add padding to simplify indexing
    heightmap = [[10] + line + [10] for line in heightmap]
    heightmap = [[10] * len(heightmap[0])] + heightmap + [[10] * len(heightmap[0])]
    return heightmap


def is_low_point(point, line_idx, idx):
    return (
        point < heightmap[line_idx - 1][idx]
        and point < heightmap[line_idx + 1][idx]
        and point < heightmap[line_idx][idx - 1]
        and point < heightmap[line_idx][idx + 1]
    )


def points_to_explore(line_idx, idx):
    return [(line_idx + 1, idx), (line_idx - 1, idx), (line_idx, idx + 1), (line_idx, idx - 1)]


def part_one(heightmap):
    low_points = 0
    for line_idx, line in enumerate(heightmap[1:-1], 1):
        for idx, point in enumerate(line[1:-1], 1):
            if is_low_point(point, line_idx, idx):
                low_points += 1 + point
    return low_points


def part_two(heightmap):
    basins = []
    for line_idx, line in enumerate(heightmap[1:-1], 1):
        for idx, point in enumerate(line[1:-1], 1):
            if is_low_point(point, line_idx, idx):
                basin_points = [(line_idx, idx)]
                to_explore = points_to_explore(line_idx, idx)
                while len(to_explore) > 0:
                    p = to_explore.pop()
                    if p not in basin_points and heightmap[p[0]][p[1]] < 9:
                        to_explore.extend(points_to_explore(p[0], p[1]))
                        basin_points.append(p)
                basins.append([heightmap[p[0]][p[1]] for p in basin_points])
    return prod(sorted([len(i) for i in basins])[-3:])


if __name__ == "__main__":
    heightmap = get_heightmap()
    print(f"Solution part one: {part_one(heightmap)} \nSolution part two: {part_two(heightmap)}")
