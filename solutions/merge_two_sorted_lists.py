"""Merge Two Sorted Lists (Linked List).

Problem (paraphrased):
Given the heads of two sorted singly linked lists, splice them into one sorted
list and return its head. The result should reuse the existing nodes.

Reasoning:
Because both inputs are already sorted, the smallest remaining node is always at
the front of one list or the other. So I walk a pointer down each list and at
every step attach the smaller head to the growing result, then advance past it.
When one list runs out, the other is already sorted and can be attached wholesale.

The one detail that keeps the code clean is a dummy head node. Without it the
first append is a special case, since there is no tail to attach to yet. The
dummy gives me a stable node to build from, and I return dummy.next at the end.
I relink the existing nodes rather than allocating new ones, so no extra list is
built.

Complexity:
Time O(n + m): each node from both lists is visited once.
Space O(1): only a handful of pointers, the merge happens in place.
"""

from typing import Optional


class ListNode:
    """Minimal singly linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def merge_two_lists(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # At most one list is non empty; attach whatever remains.
    tail.next = l1 if l1 is not None else l2
    return dummy.next
