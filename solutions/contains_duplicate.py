"""Contains Duplicate (Arrays / Hashing).

Problem (paraphrased):
Given a list of integers, return True if any value appears at least twice, and
False if every element is distinct.

Reasoning:
The question is really "have I seen this value before?", which a set answers in
O(1). I walk the list once, and for each value I check membership before adding
it. The first repeat lets me return immediately, so I do not always pay for a
full pass. The alternative of sorting first would be O(n log n) and would mutate
or copy the input; a set is both faster and simpler here. Comparing the size of
a set built from the list against the list length also works in one line, but
the early exit on the first duplicate is a little cheaper on average.

Complexity:
Time O(n): one pass, each lookup and insert is O(1) on average.
Space O(n): the set can grow to hold nearly every element before a repeat shows.
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False
