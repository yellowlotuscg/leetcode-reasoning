"""Reverse a Linked List (Linked List).

Problem (paraphrased):
Given the head of a singly linked list, reverse the direction of every pointer
and return the new head.

Reasoning:
Reversing a singly linked list is about flipping each next pointer in place. The
only hazard is that once I overwrite node.next I lose the rest of the list, so I
have to capture the next node before I touch the pointer. I carry three
references: prev (the part already reversed), curr (the node I am flipping), and
a saved handle to curr.next. Each step points curr back at prev, then slides all
three forward. When curr falls off the end, prev is the new head.

I prefer the iterative version over recursion here: it is O(1) space and avoids
a stack frame per node, which matters for long lists.

Complexity:
Time O(n): each node is visited once.
Space O(1): a fixed set of pointers, no extra structure.
"""

from typing import Optional


class ListNode:
    """Minimal singly linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev: Optional[ListNode] = None
    curr = head
    while curr is not None:
        next_node = curr.next  # Save before we overwrite the pointer.
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
