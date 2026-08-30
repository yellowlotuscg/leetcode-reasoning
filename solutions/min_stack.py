"""Min Stack (Stack Design).

Problem (paraphrased):
Design a stack that supports push, pop, top, and a getMin call that returns the
smallest value currently on the stack, with every operation running in constant
time.

Reasoning:
A plain stack handles push, pop, and top in O(1) already; the only hard part is
getMin. Scanning for the minimum on demand would be O(n), so instead I keep a
second stack that records the minimum as of each push. When I push a value, I
push onto the min stack the smaller of that value and the current minimum. The
two stacks stay in lockstep, so popping the value stack pops the min stack too,
and the top of the min stack is always the minimum of what remains.

Storing the running minimum per level is what keeps getMin O(1): the answer is
already sitting on top, and pops restore the previous minimum for free because
that older value is still recorded underneath.

Complexity:
Time O(1) for every operation: each is a constant number of list operations.
Space O(n): the auxiliary min stack mirrors the main stack one to one.
"""


class MinStack:
    def __init__(self):
        self._values = []
        self._mins = []

    def push(self, val: int) -> None:
        self._values.append(val)
        current_min = val if not self._mins else min(val, self._mins[-1])
        self._mins.append(current_min)

    def pop(self) -> None:
        self._values.pop()
        self._mins.pop()

    def top(self) -> int:
        return self._values[-1]

    def get_min(self) -> int:
        return self._mins[-1]
