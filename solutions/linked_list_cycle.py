"""Linked List Cycle (Floyd's Fast and Slow Pointers).

Problem (paraphrased):
Given the head of a singly linked list, decide whether it contains a cycle, that
is, whether following next pointers ever revisits a node.

Reasoning:
The obvious approach stores every visited node in a set and checks for a repeat,
which costs O(n) space. Floyd's trick removes that cost. I run two pointers, one
moving a single step and one moving two steps per iteration. If the list ends,
the fast pointer reaches None and there is no cycle. If there is a cycle, the
fast pointer eventually laps the slow one and they land on the same node, because
the gap between them shrinks by one each step once both are inside the loop.

The fast pointer is what makes this work in constant space: catching up is
guaranteed inside a loop, so meeting is proof of a cycle and falling off the end
is proof there is none.

Complexity:
Time O(n): the slow pointer advances at most n steps before the two meet or the
fast pointer exits.
Space O(1): just the two pointers.
"""

from typing import Optional


class ListNode:
    """Minimal singly linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
