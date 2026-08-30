"""Container With Most Water (Two Pointers).

Problem (paraphrased):
Given a list of non negative heights, treat each value as a vertical line on the
x axis. Pick two lines that, together with the x axis, hold the most water.
Return that maximum area. The area between lines i and j is the shorter of the
two heights times the horizontal distance j - i.

Reasoning:
Brute force checks all pairs at O(n^2). The insight that kills a dimension: area
is bounded by the shorter line. Start with the widest possible container, one
pointer at each end, and walk them inward. At each step width can only shrink,
so the only way to ever beat the current area is to find a taller line. Moving
the taller pointer inward can never help, because the shorter line still caps
the height while the width drops. So I always move the shorter pointer. That is
a safe greedy choice: every container I skip by doing this was already capped by
the line I am leaving behind, so none of them could have been better.

Complexity:
Time O(n): the two pointers move toward each other and together cover the array
once.
Space O(1): only a few scalars.
"""

from typing import List


def max_water_area(heights: List[int]) -> int:
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        width = right - left
        area = min(heights[left], heights[right]) * width
        if area > best:
            best = area
        # Advance the shorter side: it is the limiting factor.
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best
