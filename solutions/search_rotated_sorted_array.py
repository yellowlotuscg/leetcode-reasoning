"""Search in Rotated Sorted Array (Binary Search).

Problem (paraphrased):
A sorted array of distinct integers has been rotated at some unknown pivot, for
example [4, 5, 6, 7, 0, 1, 2]. Given a target, return its index, or -1 if it is
not present. The expected cost is O(log n).

Reasoning:
O(log n) on an array rules out a linear scan and points straight at binary
search. The complication is the rotation: the whole array is not sorted, so the
usual midpoint comparison is not enough. The saving observation is that when you
split a rotated sorted array at any midpoint, at least one of the two halves is
itself properly sorted.

So at each step I work out which half is sorted by comparing the midpoint to the
left end. If the left half is sorted, I can tell in O(1) whether the target lies
within its known range and discard the other half. If the right half is sorted,
I do the mirror check. Either way I halve the search space each iteration, which
preserves the log behavior.

Complexity:
Time O(log n): the search range halves every iteration.
Space O(1): iterative, only index variables.
"""

from typing import List


def search_rotated(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            # Left half is sorted.
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted.
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
