"""Group Anagrams (Arrays / Hashing).

Problem (paraphrased):
Given a list of strings, collect them into groups where every string in a group
is an anagram of the others. Return the groups in any order.

Reasoning:
Two strings are anagrams exactly when they share the same multiset of letters.
So I need a canonical key that is identical for anagrams and different for
everything else. Sorting the characters gives one: "eat" and "tea" both sort to
"aet". I bucket each word under its sorted form using a dictionary, then return
the buckets.

I could instead key on a 26 element count vector, which avoids the sort and
makes the per word cost O(k) rather than O(k log k). I kept the sorted key here
because it is shorter and the difference rarely matters for typical word
lengths. The count vector is the right move if k is large.

Complexity:
Let n be the number of words and k the maximum word length.
Time O(n * k log k): sorting each word dominates.
Space O(n * k): every character is stored once across the buckets.
"""

from collections import defaultdict
from typing import Dict, List


def group_anagrams(words: List[str]) -> List[List[str]]:
    buckets: Dict[str, List[str]] = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        buckets[key].append(word)
    return list(buckets.values())
