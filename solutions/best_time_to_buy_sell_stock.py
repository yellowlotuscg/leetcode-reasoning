"""Best Time to Buy and Sell Stock (One Pass).

Problem (paraphrased):
Given daily prices for a stock, find the largest profit from buying on one day
and selling on a later day. If no later day beats an earlier one, the profit is
zero.

Reasoning:
The buy has to come before the sell, so as I scan left to right I keep the
cheapest price seen so far. That lowest price is the best day I could have
bought on up to now. For each new day I ask what selling today would earn
against that minimum, and I keep the largest such profit. One pass is enough
because the running minimum already captures the best buy point behind me, so I
never need to look backward.

This is essentially Kadane's idea applied to price differences: track the best
opportunity ending at the current day while carrying the best buy point along.

Complexity:
Time O(n): a single pass over the prices.
Space O(1): two scalars, the running minimum and the best profit.
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    lowest = float("inf")
    best = 0
    for price in prices:
        if price < lowest:
            lowest = price
        elif price - lowest > best:
            best = price - lowest
    return best
