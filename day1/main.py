from typing import List
from collections import defaultdict
import functools

# 199  A
# 200  A B
# 208  A B C
# 210    B C D
# 200  E   C D
# 207  E F   D
# 240  E F G
# 269    F G H
# 260      G H
# 263        H

if __name__ == "__main__":
    levels = list()
    with open("./data-2.txt", "r") as reader:
        lines = reader.read().splitlines()
        levels = [int(line) for line in lines]

    # first step
    # decrease_count = 0
    # prev = 0
    # for curr in range(1, len(levels)):
    #     if levels[prev] < levels[curr]:
    #         decrease_count += 1
    #     prev = curr

    decrease_count = 0
    levels_len = len(levels)
    prev = sum(levels[0:3])
    for i in range(1, levels_len):
        curr = sum(levels[i:i + 3])
        if prev < curr:
            decrease_count += 1
        prev = curr
    print(decrease_count)