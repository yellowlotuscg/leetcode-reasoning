"""Validate Binary Search Tree (Bounds Recursion).

Problem (paraphrased):
Given the root of a binary tree, decide whether it is a valid binary search
tree: every node's value must be greater than all values in its left subtree and
less than all values in its right subtree.

Reasoning:
A common mistake is to check only that each node sits between its immediate
children. That is too weak: a deep descendant can violate the order even when
every parent and child pair looks fine. The correct invariant is that each node
must fall within an open range inherited from its ancestors. The root may be
anything; moving left tightens the upper bound to the parent's value, and moving
right tightens the lower bound. A node is valid only if it lies strictly inside
its current range, and then its children are checked against the narrowed bounds.

Carrying the bounds down the recursion is what turns a local check into a global
one, since each node now answers to every ancestor, not just its parent.

Complexity:
Time O(n): each node is visited once.
Space O(h) where h is the tree height, for the recursion stack. That is O(log n)
when balanced and O(n) in the worst case of a degenerate tree.
"""

from typing import Optional


class TreeNode:
    """Minimal binary tree node."""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def within(
        node: Optional[TreeNode], low: float, high: float
    ) -> bool:
        if node is None:
            return True
        if not low < node.val < high:
            return False
        # Left subtree must stay below this node; right subtree above it.
        return within(node.left, low, node.val) and within(
            node.right, node.val, high
        )

    return within(root, float("-inf"), float("inf"))
