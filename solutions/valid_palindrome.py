"""Valid Palindrome (Two Pointers).

Problem (paraphrased):
Given a string, decide whether it reads the same forward and backward once we
ignore case and consider only letters and digits. Punctuation and spaces do not
count.

Reasoning:
A palindrome check is symmetric, so I compare the ends and work inward with two
pointers. The wrinkle is that only alphanumeric characters matter, so each
pointer skips over anything that is not a letter or digit before a comparison.
When both pointers land on real characters I compare them case insensitively; a
mismatch means it is not a palindrome. If the pointers meet or cross without a
mismatch, every meaningful pair matched.

Doing the filtering inline with the two pointers keeps the work to a single pass
and avoids building a cleaned copy of the string, so the extra space stays
constant.

Complexity:
Time O(n): each pointer advances through the string at most once.
Space O(1): comparisons happen in place with no auxiliary string.
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        # Skip non alphanumeric characters from each side.
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
