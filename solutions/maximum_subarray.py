"""Maximum Subarray (Kadane's Algorithm).

Problem (paraphrased):
Given a list of integers, find the contiguous subarray with the largest sum and
return that sum. The subarray must hold at least one element.

Reasoning:
The insight is to ask, for each position, what the best subarray ending exactly
here is. That has a clean recurrence: either I extend the best subarray ending at
the previous position, or I start fresh at the current element. I start fresh
whenever the running sum has gone negative, because a negative prefix can only
drag down whatever follows. I keep a separate best-so-far that records the
largest ending sum seen anywhere.

This is Kadane's algorithm, and it is greedy in a justified way: dropping a
negative running total is always correct, since carrying it forward never helps.

Complexity:
Time O(n): one pass over the list.
Space O(1): two scalars, the current running sum and the best seen.
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    best = nums[0]
    current = nums[0]
    for value in nums[1:]:
        # Either extend the previous run or start over at this element.
        current = max(value, current + value)
        best = max(best, current)
    return best
