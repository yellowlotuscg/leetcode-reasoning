# leetcode-reasoning

A small set of classic algorithm problems worked through end to end, with the
reasoning written down rather than just the answer. The point is not the
solutions themselves, which are well known, but the path to them: how I read a
prompt, find the property that makes it tractable, and choose a structure that
hits the target complexity.

This is a case study from [Yellow Lotus Consulting Group](https://yellowlotuscg.com).
These are practice problems chosen to show problem-solving across a spread of
patterns. They are not client work.

## How I approach a problem

The same few steps cover most of these:

1. **Read the prompt carefully and restate it.** Each solution file opens with
   the problem in my own words. If I cannot restate it cleanly, I do not
   understand it yet, and the constraints (sorted? distinct? can values repeat?)
   usually point at the answer.
2. **Find the invariant.** Most of these collapse once you name the property
   that holds at every step: the partner of `x` is always `target - x`, area is
   bounded by the shorter line, the next bracket to close is the most recent one
   opened. That observation is what removes a dimension of work.
3. **Pick the simplest structure that hits the target complexity.** A stated
   bound like O(log n) is a strong hint at the technique. When there is no
   stated bound, I reach for the plainest structure (a hash map, a stack, a
   single window) that gets the job done, and only get clever when the input
   size demands it.
4. **Test the edges.** Empty input, a single element, no valid answer, and
   inputs built specifically to defeat a naive greedy approach. Those are the
   cases that catch real bugs, so the test suite leans on them.

## Problems

| # | Problem | Pattern | Time | Space |
|---|---------|---------|------|-------|
| 1 | Two Sum | Arrays / Hashing | O(n) | O(n) |
| 2 | Group Anagrams | Arrays / Hashing | O(n * k log k) | O(n * k) |
| 3 | Container With Most Water | Two Pointers | O(n) | O(1) |
| 4 | Longest Substring Without Repeating Characters | Sliding Window | O(n) | O(min(n, a)) |
| 5 | Valid Parentheses | Stack | O(n) | O(n) |
| 6 | Search in Rotated Sorted Array | Binary Search | O(log n) | O(1) |
| 7 | Reverse a Linked List | Linked List | O(n) | O(1) |
| 8 | Binary Tree Level Order Traversal | Trees (BFS) | O(n) | O(n) |
| 9 | Number of Islands | Graphs (DFS) | O(r * c) | O(r * c) |
| 10 | Coin Change | Dynamic Programming | O(amount * k) | O(amount) |
| 11 | Contains Duplicate | Arrays / Hashing | O(n) | O(n) |
| 12 | Product of Array Except Self | Prefix / Suffix Products | O(n) | O(1) |
| 13 | Top K Frequent Elements | Hashing + Bucket Sort | O(n) | O(n) |
| 14 | 3Sum | Sorting + Two Pointers | O(n^2) | O(1) |
| 15 | Valid Palindrome | Two Pointers | O(n) | O(1) |
| 16 | Best Time to Buy and Sell Stock | One Pass | O(n) | O(1) |
| 17 | Min Stack | Stack Design | O(1) per op | O(n) |
| 18 | Daily Temperatures | Monotonic Stack | O(n) | O(n) |
| 19 | Merge Two Sorted Lists | Linked List | O(n + m) | O(1) |
| 20 | Linked List Cycle | Fast / Slow Pointers | O(n) | O(1) |
| 21 | Validate Binary Search Tree | Trees (Bounds Recursion) | O(n) | O(h) |
| 22 | Course Schedule | Graphs (Cycle Detection) | O(V + E) | O(V + E) |
| 23 | House Robber | Dynamic Programming | O(n) | O(1) |
| 24 | Maximum Subarray | Greedy (Kadane) | O(n) | O(1) |

For problem 2, `k` is the maximum word length. For problem 4, `a` is the
alphabet size. For problems 9 and 10, `r` and `c` are the grid dimensions, `k`
is the number of coins. For problem 14, the O(1) space excludes the output and
the sort's internal use. For problem 19, `n` and `m` are the two list lengths.
For problem 21, `h` is the tree height, O(log n) when balanced and O(n) when
degenerate. For problem 22, `V` is the number of courses and `E` the number of
prerequisites.

## Layout

```
leetcode-reasoning/
├── solutions/                 one module per problem
│   ├── two_sum.py
│   ├── group_anagrams.py
│   ├── container_with_most_water.py
│   ├── longest_substring_without_repeating.py
│   ├── valid_parentheses.py
│   ├── search_rotated_sorted_array.py
│   ├── reverse_linked_list.py
│   ├── binary_tree_level_order.py
│   ├── number_of_islands.py
│   ├── coin_change.py
│   ├── contains_duplicate.py
│   ├── product_except_self.py
│   ├── top_k_frequent.py
│   ├── three_sum.py
│   ├── valid_palindrome.py
│   ├── best_time_to_buy_sell_stock.py
│   ├── min_stack.py
│   ├── daily_temperatures.py
│   ├── merge_two_sorted_lists.py
│   ├── linked_list_cycle.py
│   ├── validate_bst.py
│   ├── course_schedule.py
│   ├── house_robber.py
│   └── maximum_subarray.py
├── tests/
│   └── test_solutions.py      pytest, several cases per problem
├── conftest.py                puts the repo root on sys.path
├── LICENSE
└── README.md
```

Each solution module carries the problem statement in my own words, a short
reasoning section on why I chose the approach, and the time and space
complexity with a one line justification.

## Running the tests

From the repo root:

```
python -m pytest
```

The solutions target Python 3.9 and use only the standard library.
