"""House Robber (1D Dynamic Programming).

Problem (paraphrased):
Given a list of non negative amounts in houses along a street, find the most you
can take without robbing two adjacent houses.

Reasoning:
At each house I face one of two choices: skip it, keeping whatever I had through
the previous house, or rob it, adding its amount to the best total from two
houses back (since the immediate neighbor is then off limits). So the best total
through house i is the larger of "best through i - 1" and "amount[i] plus best
through i - 2". That recurrence is the whole problem.

I only ever look two steps back, so I do not need a full table, just two rolling
values: the best totals ending at the previous house and the one before it. I
slide them forward as I go, which keeps the space constant.

Complexity:
Time O(n): one pass over the houses.
Space O(1): two rolling totals instead of a full DP array.
"""

from typing import List


def rob(nums: List[int]) -> int:
    # prev2 is the best through house i - 2, prev1 through house i - 1.
    prev2 = 0
    prev1 = 0
    for amount in nums:
        take = prev2 + amount
        skip = prev1
        prev2 = prev1
        prev1 = max(take, skip)
    return prev1
