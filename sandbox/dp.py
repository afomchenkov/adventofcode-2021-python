from collections import defaultdict, deque
from functools import partial, cache


"""
    Given a matrix m x n, how many possible paths from right top corner to left bottom corner
    You can go only right and down

    Example count:
    .  .  .  .  .  .  .
    28 21 15 10 6  3  1
    7  6  5  4  3  2  1
    1  1  1  1  1  1  1

    Time complexity: O(m * n)
    Space complexity: O(1)
"""
def uniquie_path(m: int, n: int) -> int:
    row = [1] * n

    for i in range(m - 1):
        new_row = [1] * n
        for j in range(n - 2, -1, -1):
            new_row[j] = new_row[j + 1] + row[j]
        row = new_row

    return row[0]


"""
    Given two strings, return the length of their longest common subsequence

    Example:
    s1 = abcde
    s2 = ace
    result = 3

    Bottom-up DP approach
            j
          a c e .
       a  1
       b    0
    i  c    1
       d      0
       e      1
          . . . .

    Time complexity: O(m * n)
    Space complexity: O(m * n)
"""
def longest_subseq(str1: str, str2: str) -> int:
    dp = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(len(str1) - 1, -1, -1):
        for j in range(len(str2) - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]


"""
    Best time to buy and sell stock with cooldown
    Given prices[i], ith price of a given stock, find max profit
    after you sell stock, you cannot buy stock next day

    Example:
    prices = [1, 2, 3, 0, 2]
    output: 3
    transactions = [buym sell, cooldown, buy, sell]
"""
def buy_sell_stock(prices: list[int]) -> int:
    # state: buying or selling
    # if buy -> i + 1
    # if sell -> i + 2
    dp = {} # key=(i, buying) val=max_profit

    def dfs(i, buying):
        if i >= len(prices):
            return 0
        if (i, buying) in dp:
            return dp[(i, buying)]

        cooldown = dfs(i + 1, buying)
        if buying:
            buy = dfs(i + 1, not buying) - prices[i]
            dp[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i + 2, not buying) + prices[i]
            dp[(i, buying)] = max(sell, cooldown)

        return dp[(i, buying)]
    return dfs(0, True)

if __name__ == "__main__":
    pass
