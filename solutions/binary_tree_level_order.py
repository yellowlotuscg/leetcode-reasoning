"""Binary Tree Level Order Traversal (Trees, BFS).

Problem (paraphrased):
Given the root of a binary tree, return its values grouped by depth: a list of
lists, where the first inner list is the root level, the next is its children,
and so on from top to bottom.

Reasoning:
"Group nodes by level" is breadth first search. The detail that makes the output
clean is processing the tree one level at a time rather than node by node. At
the top of each loop I record how many nodes are currently in the queue: that
count is exactly the current level. I drain precisely that many nodes into one
sublist while enqueuing their children, which become the next level. Snapshotting
the count keeps levels from bleeding into each other even as I push children
onto the same queue.

I use collections.deque so popping from the front is O(1); a plain list would
make that O(n).

Complexity:
Time O(n): every node is enqueued and dequeued once.
Space O(n): the queue holds at most one level, which can be up to about half the
nodes in a full tree, and the output stores every value.
"""

from collections import deque
from typing import List, Optional


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


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    levels: List[List[int]] = []
    queue = deque([root])
    while queue:
        level_size = len(queue)  # Nodes belonging to the current level.
        current_level: List[int] = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        levels.append(current_level)
    return levels
