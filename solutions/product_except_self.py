"""Product of Array Except Self (Prefix / Suffix Products).

Problem (paraphrased):
Given a list of integers, return a list where each position holds the product of
every other element. Division is not allowed, and the intended runtime is linear.

Reasoning:
Without division, the product at position i is everything to its left times
everything to its right. Both of those are running products, so I can compute
them in two passes. First I sweep left to right, storing in result[i] the
product of all elements before i. Then I sweep right to left carrying a running
suffix product and multiply it into each result[i]. After the second pass each
slot holds left product times right product, which is exactly the product of all
the other elements.

I avoid division deliberately: it would break on a zero in the input, and the
prefix/suffix idea sidesteps that entirely. I keep the suffix product in a single
variable rather than a second array so the only allocation is the output itself.

Complexity:
Time O(n): two linear passes.
Space O(1) beyond the output list, which the problem requires me to return.
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    # First pass: result[i] holds the product of everything to the left of i.
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Second pass: fold in the product of everything to the right of i.
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
