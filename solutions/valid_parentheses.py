"""Valid Parentheses (Stack).

Problem (paraphrased):
Given a string containing only the bracket characters (), [], and {}, decide
whether they are balanced. Every opening bracket must be closed by the matching
type, and brackets must close in the correct order.

Reasoning:
Matching is last in, first out: the most recently opened bracket is the one that
has to close next. That ordering is exactly what a stack models. I push every
opening bracket. On a closing bracket I check that the top of the stack is its
matching opener; if it is not, or the stack is empty, the string is invalid. At
the end a balanced string leaves the stack empty, so any leftover openers also
fail.

I keep a small map from closing to opening bracket so the check is a single
lookup rather than a branch per pair.

Complexity:
Time O(n): each character is pushed or popped at most once.
Space O(n): a string of all openers fills the stack.
"""


def is_valid_parentheses(text: str) -> bool:
    closing_to_opening = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in text:
        if char in closing_to_opening:
            # Closing bracket: top must be the matching opener.
            if not stack or stack.pop() != closing_to_opening[char]:
                return False
        else:
            stack.append(char)
    return not stack
