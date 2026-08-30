"""Two Sum (Arrays / Hashing).

Problem (paraphrased):
Given a list of integers and a target value, return the indices of the two
numbers that add up to the target. Exactly one valid pair is guaranteed, and
the same element cannot be used twice.

Reasoning:
The brute force is to check every pair, which is O(n^2). The thing to notice is
that for any number x, its partner is fully determined: it has to be
target - x. So the real question per element is "have I already seen the value
I need?". A hash map answers that in O(1). I walk the list once, and before
storing the current value I check whether its complement is already in the map.
That turns the nested scan into a single pass. I store value -> index so I can
return positions, not values.

Complexity:
Time O(n): one pass, each lookup and insert is O(1) on average.
Space O(n): in the worst case the map holds nearly every element before the
match is found.
"""

from typing import Dict, List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen: Dict[int, int] = {}
    for i, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], i]
        seen[value] = i
    # Per the problem a solution always exists, so this is unreachable.
    return []
