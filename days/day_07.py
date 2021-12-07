from time import time


def move_linear(current: int, to: int):
    return abs(current - to)


def move_increment(current: int, to: int):
    moves = abs(current - to)
    return sum(range(moves + 1))


def part_1(crabs: list[int]):
    left = min(crabs)
    right = max(crabs) + 1

    least_fuel = right * len(crabs)
    for position in range(left, right):
        fuel_cost = sum([move_linear(current=crab, to=position) for crab in crabs])
        if fuel_cost < least_fuel:
            least_fuel = fuel_cost

    return least_fuel


def part_2(crabs: list[int]):
    left = min(crabs)
    right = max(crabs) + 1

    least_fuel = 9e20  # big number

    for position in range(left, right):
        fuel_cost = sum([move_increment(current=crab, to=position) for crab in crabs])
        if fuel_cost < least_fuel:
            least_fuel = fuel_cost

    return least_fuel


if __name__ == "__main__":
    with open("day_07.txt", "r") as f:
        input_data = list(map(int, f.read().split(",")))

    answer_1 = part_1(input_data)
    print(answer_1)
    start = time()
    answer_2 = part_2(input_data)
    end = time()
    print(answer_2)
