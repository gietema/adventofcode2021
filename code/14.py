from collections import defaultdict
from pathlib import Path


def get_answer(counts: dict[str, int], template: str) -> int:
    character_counts = defaultdict(lambda: 0)
    for key, value in counts.items():
        character_counts[key[0]] += value
    character_counts[template[-1]] += 1
    counts = sorted(list(character_counts.values()))
    return counts[-1] - counts[0]


def get_counts(steps: int, counts: dict[str, int], rules: dict[str, str]) -> dict[str, int]:
    for i in range(steps):
        new_counts = defaultdict(lambda: 0)
        for key, count in counts.items():
            new_counts[key[0] + rules[key]] += count
            new_counts[rules[key] + key[1]] += count
        counts = new_counts
    return counts


if __name__ == "__main__":
    inp = [line.rstrip() for line in open(Path(__file__).parent.parent / "input" / "14.txt")]
    polymer_template = inp[0]
    insertion_rules = {rule[0]: rule[1] for rule in [line.split(" -> ") for line in inp[2:]]}
    pairs = [polymer_template[idx : idx + 2] for idx in range(len(polymer_template) - 1)]
    initial_counts = {key: pairs.count(key) for key in insertion_rules}
    print(
        f"Solution part one: {get_answer(get_counts(10, initial_counts, insertion_rules), polymer_template)}\n"
        f"Solution part two: {get_answer(get_counts(40, initial_counts, insertion_rules), polymer_template)}"
    )
