"""Top K Frequent Elements (Hashing + Bucket Sort).

Problem (paraphrased):
Given a list of integers and a number k, return the k values that occur most
often. The answer is guaranteed to be unique, and order among the k does not
matter.

Reasoning:
The first step is to count occurrences, which a hash map does in one pass. The
naive follow up is to sort the values by count, which is O(n log n). I can do
better because a count is bounded: no value can appear more than n times. That
lets me bucket by frequency. I build a list of buckets indexed by count, drop
each value into the bucket matching its frequency, then walk the buckets from
highest count down, collecting values until I have k. Since the buckets are
indexed by an integer in a fixed range, this avoids a comparison sort entirely.

Complexity:
Time O(n): counting is one pass, and the buckets hold n values total to scan.
Space O(n): the count map and the buckets together hold every distinct value.
"""

from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    counts = Counter(nums)

    # buckets[f] holds every value that occurs exactly f times. A value can
    # appear at most len(nums) times, so this many buckets is enough.
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for value, freq in counts.items():
        buckets[freq].append(value)

    result: List[int] = []
    for freq in range(len(buckets) - 1, 0, -1):
        for value in buckets[freq]:
            result.append(value)
            if len(result) == k:
                return result
    return result
