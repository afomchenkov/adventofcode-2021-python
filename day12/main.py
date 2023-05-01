from typing import List
from collections import namedtuple
from dataclasses import dataclass

if __name__ == "__main__":
    with open("./data-1.txt", "r") as reader:
        lines = reader.read().splitlines()
        lines = [point.split('-') for point in lines]

        print(lines)
