"""Coin Change (Dynamic Programming).

Problem (paraphrased):
Given a list of distinct coin denominations and a target amount, return the
fewest coins that sum to that amount. Coins may be reused without limit. If the
amount cannot be made from the given coins, return -1.

Reasoning:
A greedy "take the largest coin that fits" approach is wrong for arbitrary
denominations: with coins [1, 3, 4] and amount 6, greedy gives 4 + 1 + 1 (three
coins) but 3 + 3 (two coins) is better. So I need to actually consider
combinations, and the structure is naturally recursive: the best way to make
amount n is one coin c plus the best way to make n - c, minimized over the coins
that fit. Those subproblems overlap heavily, which is the signal for dynamic
programming.

I build a table bottom up. best[a] is the minimum coins to make amount a. I seed
best[0] = 0 (zero coins make zero) and treat every other amount as unreachable
until proven otherwise. For each amount I try every coin and keep the cheapest
option. If the target is still unreachable at the end, I return -1.

Complexity:
Time O(amount * k) where k is the number of coins: each amount tries every coin.
Space O(amount): one entry per sub amount up to the target.
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    # Sentinel larger than any real answer; amount + 1 coins is impossible.
    unreachable = amount + 1
    best = [0] + [unreachable] * amount

    for current in range(1, amount + 1):
        for coin in coins:
            if coin <= current:
                best[current] = min(best[current], best[current - coin] + 1)

    return best[amount] if best[amount] != unreachable else -1
