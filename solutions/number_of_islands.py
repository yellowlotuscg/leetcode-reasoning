"""Number of Islands (Graphs).

Problem (paraphrased):
Given a 2D grid where each cell is "1" for land or "0" for water, count the
islands. An island is a group of land cells connected horizontally or
vertically (not diagonally). The grid edges are surrounded by water.

Reasoning:
The grid is a graph in disguise: each land cell is a node, and edges connect it
to its land neighbors up, down, left, and right. Counting islands is counting
connected components. The plan is to scan the grid, and each time I hit a piece
of land I have not visited, that is a new island, so I increment the count and
then flood the entire connected blob so I never count it again.

I flood with an iterative depth first search using an explicit stack. Recursion
reads a little cleaner but risks hitting Python's recursion limit on a large
solid grid, so I keep the stack on the heap. I mark visited cells by overwriting
them with "0" in place, which doubles as the water check and avoids a separate
visited set.

Complexity:
Time O(r * c): every cell is examined a constant number of times.
Space O(r * c): the worst case stack holds a large fraction of the cells when the
grid is mostly land.
"""

from typing import List


def count_islands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def sink(start_r: int, start_c: int) -> None:
        # Iterative DFS that flips a whole connected blob of land to water.
        stack = [(start_r, start_c)]
        while stack:
            r, c = stack.pop()
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue
            if grid[r][c] != "1":
                continue
            grid[r][c] = "0"  # Mark visited.
            stack.append((r + 1, c))
            stack.append((r - 1, c))
            stack.append((r, c + 1))
            stack.append((r, c - 1))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                sink(r, c)
    return islands
