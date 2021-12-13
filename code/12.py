from dataclasses import dataclass
from pathlib import Path
from typing import Optional


def get_caves() -> dict[str, str]:
    caves = {}
    for base in [f.rstrip().split("-") for f in open(Path(__file__).parent.parent / "input" / "12.txt")]:
        caves.setdefault(base[0], [])
        caves[base[0]].append(base[1])
        if base[1] != "end" and base[0] != "start":
            caves.setdefault(base[1], [])
            caves[base[1]].append(base[0])
    return caves


CAVES = get_caves()
SMALL_CAVES = [cave for cave in CAVES if cave.islower() and cave not in ["end", "start"]]


@dataclass
class Cave:
    name: str
    previous: Optional["Cave"] = None

    @property
    def paths(self) -> list["Cave"]:
        return [Cave(path_name, previous=self) for path_name in CAVES[self.name] if path_name != "start"]

    def route(self) -> list[str]:
        route, prev = [], self.previous
        while prev is not None:
            route.append(prev.name)
            prev = prev.previous
        return route[::-1]


def has_double(route: list[str], small_caves: list[str]) -> bool:
    return any([route.count(cave) == 2 for cave in small_caves])


def find_routes(cave: Cave, visit_single_twice: bool = False) -> int:
    routes, caves = 0, cave.paths
    while len(caves) > 0:
        cave = caves.pop()
        if cave.name == "end":
            routes += 1
        elif (
            (cave.name not in SMALL_CAVES)
            or (cave.name not in (route := cave.route()))
            or (route.count(cave.name) == 1 and not has_double(route, SMALL_CAVES) and visit_single_twice)
        ):
            caves.extend(cave.paths)
    return routes


if __name__ == "__main__":
    print(f"Solution part one: {find_routes(Cave('start'))}")
    print(f"Solution part two: {find_routes(Cave('start'), True)}")
