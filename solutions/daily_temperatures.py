"""Daily Temperatures (Monotonic Stack).

Problem (paraphrased):
Given a list of daily temperatures, return for each day how many days you must
wait for a warmer temperature. If no warmer day comes, the answer for that day
is zero.

Reasoning:
The brute force compares each day against all later days, which is O(n^2). The
key observation is that once I see a warmer day, it resolves every earlier day
that was still waiting and is colder than it. That "resolve the most recent
unresolved items first" pattern is a stack.

I keep a stack of indices whose answers are still open, and it stays decreasing
in temperature from bottom to top. For each new day I pop every index on the
stack that is colder than today, filling in its answer as the distance to today,
then push today. Each index is pushed and popped at most once, so the whole
thing is linear despite the inner while loop.

Complexity:
Time O(n): every index enters and leaves the stack at most once.
Space O(n): the stack can hold every day in a strictly decreasing run.
"""

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack: List[int] = []  # Indices of days still waiting for a warmer one.

    for day, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            earlier = stack.pop()
            answer[earlier] = day - earlier
        stack.append(day)

    return answer
