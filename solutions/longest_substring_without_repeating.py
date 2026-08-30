"""Longest Substring Without Repeating Characters (Sliding Window).

Problem (paraphrased):
Given a string, find the length of the longest contiguous run of characters that
contains no repeats.

Reasoning:
A "longest contiguous run that satisfies a property" problem is the textbook cue
for a sliding window. I keep a window [start, end] that is always valid, meaning
it has no duplicate character. I extend the right edge one character at a time.
When the new character is already inside the window, the window is no longer
valid, so I move the left edge forward just enough to drop the earlier
occurrence.

The trick that makes this one pass instead of two is remembering the last index
where each character appeared. When I hit a repeat, I can jump start directly
past the previous occurrence rather than sliding it one position at a time. I
guard with max() so a stale index from outside the current window never drags
start backward.

Complexity:
Time O(n): each character is visited once on the right edge; start only moves
forward.
Space O(min(n, a)) where a is the alphabet size: the map holds at most one entry
per distinct character.
"""

from typing import Dict


def length_of_longest_unique_substring(text: str) -> int:
    last_seen: Dict[str, int] = {}
    start = 0
    longest = 0
    for end, char in enumerate(text):
        if char in last_seen and last_seen[char] >= start:
            # Skip the window past the previous occurrence of this char.
            start = last_seen[char] + 1
        last_seen[char] = end
        current_length = end - start + 1
        if current_length > longest:
            longest = current_length
    return longest
