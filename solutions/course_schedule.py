"""Course Schedule (Graph, Cycle Detection via DFS).

Problem (paraphrased):
Given a number of courses labeled 0 to n - 1 and a list of prerequisite pairs
(a, b) meaning b must be taken before a, decide whether it is possible to finish
every course.

Reasoning:
Each prerequisite is a directed edge, so the courses form a directed graph and
the question is whether that graph has a cycle. If a cycle exists, the courses in
it depend on each other and none can be taken first, so the answer is no.
Otherwise a valid order exists.

I detect cycles with a depth first search that colors nodes in three states:
unvisited, in progress (on the current recursion path), and done. Reaching a node
that is still in progress means I have looped back on myself, which is a cycle.
Once a node's whole subtree is explored without trouble I mark it done so I never
re-explore it, which keeps the search linear. This is the standard topological
feasibility check; I do not need the order itself, only whether one exists.

Complexity:
Time O(V + E): each course and each prerequisite edge is examined once.
Space O(V + E): the adjacency list holds every edge, plus O(V) for the state
array and the recursion stack.
"""

from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph: List[List[int]] = [[] for _ in range(num_courses)]
    for course, needed in prerequisites:
        graph[course].append(needed)

    # 0 unvisited, 1 in progress on the current path, 2 fully explored.
    state = [0] * num_courses

    def has_cycle(course: int) -> bool:
        if state[course] == 1:
            return True
        if state[course] == 2:
            return False
        state[course] = 1
        for needed in graph[course]:
            if has_cycle(needed):
                return True
        state[course] = 2
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False
    return True
