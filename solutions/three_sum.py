"""3Sum (Sorting + Two Pointers).

Problem (paraphrased):
Given a list of integers, return all unique triples that sum to zero. The
returned triples must not repeat, even though the same value may appear more
than once in the input.

Reasoning:
Sorting first is what makes this tractable. Once the list is sorted I fix one
number and look for two others to its right that, with it, sum to zero. With a
sorted tail, that inner search is the classic two pointer scan: if the running
sum is too small I move the left pointer up, if it is too large I move the right
pointer down, and when it hits zero I record the triple.

The fiddly part is duplicates. I skip a fixed value if it equals the one before
it, so I never start the same triple twice. After recording a hit I also advance
both pointers past any runs of equal values. Sorting groups duplicates together,
which is exactly what makes these skips a simple equality check against the
neighbor.

Complexity:
Time O(n^2): the sort is O(n log n), then each fixed value drives a linear two
pointer scan, n of them.
Space O(1) beyond the output and whatever the sort uses internally.
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triples: List[List[int]] = []
    n = len(nums)

    for i in range(n - 2):
        # The smallest fixed value is positive, so no triple can reach zero.
        if nums[i] > 0:
            break
        # Skip a repeated fixed value to avoid duplicate triples.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triples.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Step past duplicate values on both sides.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return triples
