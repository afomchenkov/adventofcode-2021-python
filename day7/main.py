from typing import List
from collections import namedtuple
from dataclasses import dataclass

if __name__ == "__main__":
    with open("./data-2.txt", "r") as reader:
        lines = reader.read().splitlines()
        values = [int(val) for val in lines[0].split(',')]

        default_max = 100000000

        srt = sorted(values)
        unique = set(srt)
        # [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        # [0, 1, 1, 2, 2, 2, 4, 7, 14, 16]
        # {0, 1, 2, 4, 7, 14, 16}

        sum_of_steps = lambda n: int(n * (n + 1) / 2)
        cache_step = dict()
        for i in range(0, max(unique) + 1):
            cache_step[f'{i}'] = sum_of_steps(i)

        def get_spend_amount(begin, end):
            step_key = f'{end - begin}'
            return cache_step[step_key]

        min_value = [default_max, -1]
        for base in range(min(unique), max(unique)):
            min_here = 0
            for value in srt:
                min_here += get_spend_amount(min(base, value), max(base, value))
                # min_here += abs(base - value)
            if min_here < min_value[0]:
                min_value[0] = min_here
                min_value[1] = base

        print(min_value)
