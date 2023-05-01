from typing import List
from collections import namedtuple
from dataclasses import dataclass


def parse_common(bit: List[int]):
    return 0 if bit[0] > bit[1] else 1


def parse_uncommon(bit: List[int]):
    return 0 if bit[0] < bit[1] else 1


def to_int(bitlist: List[int]) -> int:
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out


def calculate_bits(grid: List[List[int]], registry_len: int):
    # [i, j] - bits occurrences
    common_bits = [[0, 0] for _ in range(registry_len)]
    for row in grid:
        for i in range(0, len(row)):
            common_bits[i][row[i]] += 1

    common = [parse_common(bit) for bit in common_bits]
    uncommon = [parse_uncommon(bit) for bit in common_bits]

    return (common, uncommon, common_bits)


def oxygen_rating(bits: List[List[int]], bits_config: List[List[int]]):
    filtered_bits = list(bits)

    def _filter(index: int, bits: List[List[int]], config: List[List[int]]):
        if index == len(config[0]) or len(bits) == 1:
            return bits[0]

        if config[2][index][0] == config[2][index][1]:
            bits = [*filter(lambda b: (b[index] == 1), bits)]
        else:
            bits = [*filter(lambda b: (b[index] == config[0][index]), bits)]

        config = calculate_bits(bits, len(bits[0]))
        return _filter(index + 1, bits, config)

    return _filter(0, filtered_bits, bits_config)


def co2_rating(bits: List[List[int]], bits_config: List[List[int]]):
    filtered_bits = list(bits)

    def _filter(index: int, bits: List[List[int]], config: List[List[int]]):
        if index == len(config[0]) or len(bits) == 1:
            return bits[0]

        if config[2][index][0] == config[2][index][1]:
            bits = [*filter(lambda b: (b[index] == 0), bits)]
        else:
            bits = [*filter(lambda b: (b[index] == config[1][index]), bits)]

        config = calculate_bits(bits, len(bits[0]))
        return _filter(index + 1, bits, config)

    return _filter(0, filtered_bits, bits_config)


if __name__ == "__main__":
    grid = [[]]
    with open("./data-2.txt", "r") as reader:
        lines = reader.read().splitlines()
        grid = [[*map(int, list(line))] for line in lines]

    bits_config = calculate_bits(grid, len(grid[0]))
    common, uncommon, _ = bits_config

    print(to_int(uncommon) * to_int(common))

    oxygen = oxygen_rating(grid, bits_config)
    print('Result Oxygen: ', oxygen, to_int(oxygen))

    co2 = co2_rating(grid, bits_config)
    print('Result CO2: ', co2, to_int(co2))

    print(f'Result: {to_int(oxygen) * to_int(co2)}')
