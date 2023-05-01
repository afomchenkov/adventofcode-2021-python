from typing import List
from collections import namedtuple
from dataclasses import dataclass

if __name__ == "__main__":
    with open("./data-1.txt", "r") as reader:
        lines = reader.read().splitlines()
        lines = [line.split('|') for line in lines]
        parsed = list()
        for chunk in lines:
            [pattern, output] = chunk
            parsed.append((
                pattern.strip().split(),
                output.strip().split(),
            ))

        print(parsed)
