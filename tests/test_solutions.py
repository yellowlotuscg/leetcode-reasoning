"""Tests for the solution modules.

Several cases per problem, including the edges I would worry about in review:
empty inputs, single elements, no valid answer, and inputs that defeat a naive
greedy approach.
"""

from solutions.best_time_to_buy_sell_stock import max_profit
from solutions.binary_tree_level_order import TreeNode, level_order
from solutions.coin_change import coin_change
from solutions.container_with_most_water import max_water_area
from solutions.contains_duplicate import contains_duplicate
from solutions.course_schedule import can_finish
from solutions.daily_temperatures import daily_temperatures
from solutions.group_anagrams import group_anagrams
from solutions.house_robber import rob
from solutions.linked_list_cycle import ListNode as CycleListNode
from solutions.linked_list_cycle import has_cycle
from solutions.longest_substring_without_repeating import (
    length_of_longest_unique_substring,
)
from solutions.maximum_subarray import max_subarray
from solutions.merge_two_sorted_lists import ListNode as MergeListNode
from solutions.merge_two_sorted_lists import merge_two_lists
from solutions.min_stack import MinStack
from solutions.number_of_islands import count_islands
from solutions.product_except_self import product_except_self
from solutions.reverse_linked_list import ListNode, reverse_list
from solutions.search_rotated_sorted_array import search_rotated
from solutions.three_sum import three_sum
from solutions.top_k_frequent import top_k_frequent
from solutions.two_sum import two_sum
from solutions.valid_palindrome import is_palindrome
from solutions.valid_parentheses import is_valid_parentheses
from solutions.validate_bst import is_valid_bst


# Helpers for the linked list tests.
def build_list(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def list_to_values(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class TestTwoSum:
    def test_basic(self):
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    def test_pair_at_end(self):
        assert two_sum([3, 2, 4], 6) == [1, 2]

    def test_duplicate_values(self):
        assert two_sum([3, 3], 6) == [0, 1]

    def test_negatives(self):
        assert two_sum([-1, -2, -3, -4], -6) == [1, 3]


class TestGroupAnagrams:
    def test_basic(self):
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        normalized = sorted(sorted(group) for group in result)
        assert normalized == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

    def test_empty_string_groups_together(self):
        assert group_anagrams([""]) == [[""]]

    def test_single_word(self):
        assert group_anagrams(["a"]) == [["a"]]

    def test_no_anagrams(self):
        result = group_anagrams(["abc", "def"])
        normalized = sorted(sorted(group) for group in result)
        assert normalized == [["abc"], ["def"]]


class TestContainerWithMostWater:
    def test_basic(self):
        assert max_water_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    def test_two_lines(self):
        assert max_water_area([1, 1]) == 1

    def test_increasing(self):
        assert max_water_area([1, 2, 3, 4, 5]) == 6

    def test_tall_ends(self):
        assert max_water_area([2, 1, 1, 1, 2]) == 8


class TestLongestSubstring:
    def test_basic(self):
        assert length_of_longest_unique_substring("abcabcbb") == 3

    def test_all_same(self):
        assert length_of_longest_unique_substring("bbbbb") == 1

    def test_mixed(self):
        assert length_of_longest_unique_substring("pwwkew") == 3

    def test_empty(self):
        assert length_of_longest_unique_substring("") == 0

    def test_repeat_outside_window(self):
        # The second 'a' sits outside the current window; start must not jump back.
        assert length_of_longest_unique_substring("abba") == 2


class TestValidParentheses:
    def test_simple_pair(self):
        assert is_valid_parentheses("()") is True

    def test_mixed_types(self):
        assert is_valid_parentheses("()[]{}") is True

    def test_wrong_order(self):
        assert is_valid_parentheses("(]") is False

    def test_unbalanced_close(self):
        assert is_valid_parentheses("]") is False

    def test_unclosed_open(self):
        assert is_valid_parentheses("(") is False

    def test_empty(self):
        assert is_valid_parentheses("") is True


class TestSearchRotated:
    def test_target_present(self):
        assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4

    def test_target_absent(self):
        assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1

    def test_single_element_found(self):
        assert search_rotated([1], 1) == 0

    def test_single_element_missing(self):
        assert search_rotated([1], 0) == -1

    def test_not_actually_rotated(self):
        assert search_rotated([1, 2, 3, 4, 5], 4) == 3


class TestReverseLinkedList:
    def test_basic(self):
        head = build_list([1, 2, 3, 4, 5])
        assert list_to_values(reverse_list(head)) == [5, 4, 3, 2, 1]

    def test_single_node(self):
        head = build_list([42])
        assert list_to_values(reverse_list(head)) == [42]

    def test_empty(self):
        assert reverse_list(None) is None


class TestLevelOrder:
    def test_basic(self):
        root = TreeNode(
            3,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7)),
        )
        assert level_order(root) == [[3], [9, 20], [15, 7]]

    def test_single_node(self):
        assert level_order(TreeNode(1)) == [[1]]

    def test_empty(self):
        assert level_order(None) == []

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        assert level_order(root) == [[1], [2], [3]]


class TestNumberOfIslands:
    def test_single_island(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        assert count_islands(grid) == 1

    def test_multiple_islands(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        assert count_islands(grid) == 3

    def test_all_water(self):
        grid = [["0", "0"], ["0", "0"]]
        assert count_islands(grid) == 0

    def test_empty_grid(self):
        assert count_islands([]) == 0

    def test_diagonal_not_connected(self):
        grid = [["1", "0"], ["0", "1"]]
        assert count_islands(grid) == 2


class TestCoinChange:
    def test_basic(self):
        assert coin_change([1, 2, 5], 11) == 3

    def test_impossible(self):
        assert coin_change([2], 3) == -1

    def test_zero_amount(self):
        assert coin_change([1], 0) == 0

    def test_greedy_would_fail(self):
        # Greedy picks 4 + 1 + 1; the optimum is 3 + 3.
        assert coin_change([1, 3, 4], 6) == 2

    def test_single_coin_exact(self):
        assert coin_change([7], 14) == 2


# Helpers for the cycle list tests, which use a distinct ListNode class.
def build_cycle_list(values, cycle_index):
    nodes = [CycleListNode(value) for value in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_index is not None and nodes:
        nodes[-1].next = nodes[cycle_index]
    return nodes[0] if nodes else None


def build_merge_list(values):
    head = None
    for value in reversed(values):
        head = MergeListNode(value, head)
    return head


def merge_list_to_values(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class TestContainsDuplicate:
    def test_has_duplicate(self):
        assert contains_duplicate([1, 2, 3, 1]) is True

    def test_all_distinct(self):
        assert contains_duplicate([1, 2, 3, 4]) is False

    def test_empty(self):
        assert contains_duplicate([]) is False

    def test_single_element(self):
        assert contains_duplicate([7]) is False

    def test_all_same(self):
        assert contains_duplicate([5, 5, 5, 5]) is True


class TestProductExceptSelf:
    def test_basic(self):
        assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_with_zero(self):
        assert product_except_self([0, 4, 0]) == [0, 0, 0]

    def test_single_zero(self):
        # Only the zero's position gets the product of the rest.
        assert product_except_self([1, 2, 0, 4]) == [0, 0, 8, 0]

    def test_negatives(self):
        assert product_except_self([-1, 1, 2]) == [2, -2, -1]

    def test_two_elements(self):
        assert product_except_self([3, 5]) == [5, 3]


class TestTopKFrequent:
    def test_basic(self):
        assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]

    def test_single_element(self):
        assert top_k_frequent([1], 1) == [1]

    def test_k_equals_distinct_count(self):
        assert sorted(top_k_frequent([4, 4, 5, 6], 3)) == [4, 5, 6]

    def test_all_unique(self):
        assert sorted(top_k_frequent([7, 8, 9], 1)) in ([7], [8], [9])


class TestThreeSum:
    def normalize(self, triples):
        return sorted(sorted(triple) for triple in triples)

    def test_basic(self):
        result = three_sum([-1, 0, 1, 2, -1, -4])
        assert self.normalize(result) == [[-1, -1, 2], [-1, 0, 1]]

    def test_no_triple(self):
        assert three_sum([1, 2, 3]) == []

    def test_all_zeros_dedup(self):
        # Many zeros must yield a single triple, not one per combination.
        assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]

    def test_empty(self):
        assert three_sum([]) == []

    def test_repeated_values_dedup(self):
        result = three_sum([-2, 0, 0, 2, 2])
        assert self.normalize(result) == [[-2, 0, 2]]


class TestValidPalindrome:
    def test_alphanumeric_mixed(self):
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_not_a_palindrome(self):
        assert is_palindrome("race a car") is False

    def test_empty(self):
        assert is_palindrome("") is True

    def test_only_punctuation(self):
        assert is_palindrome(".,") is True

    def test_single_character(self):
        assert is_palindrome("z") is True


class TestMaxProfit:
    def test_basic(self):
        assert max_profit([7, 1, 5, 3, 6, 4]) == 5

    def test_decreasing(self):
        assert max_profit([7, 6, 4, 3, 1]) == 0

    def test_single_day(self):
        assert max_profit([5]) == 0

    def test_empty(self):
        assert max_profit([]) == 0

    def test_increasing(self):
        assert max_profit([1, 2, 3, 4, 5]) == 4


class TestMinStack:
    def test_min_tracks_through_pops(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        assert stack.get_min() == -3
        stack.pop()
        assert stack.get_min() == -2
        assert stack.top() == 0

    def test_single_value(self):
        stack = MinStack()
        stack.push(42)
        assert stack.get_min() == 42
        assert stack.top() == 42

    def test_duplicates_keep_min(self):
        stack = MinStack()
        stack.push(1)
        stack.push(1)
        stack.pop()
        assert stack.get_min() == 1


class TestDailyTemperatures:
    def test_basic(self):
        temps = [73, 74, 75, 71, 69, 72, 76, 73]
        assert daily_temperatures(temps) == [1, 1, 4, 2, 1, 1, 0, 0]

    def test_monotonic_increasing(self):
        assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]

    def test_no_warmer_day(self):
        assert daily_temperatures([60, 50, 40]) == [0, 0, 0]

    def test_single_day(self):
        assert daily_temperatures([50]) == [0]


class TestMergeTwoSortedLists:
    def test_basic(self):
        l1 = build_merge_list([1, 2, 4])
        l2 = build_merge_list([1, 3, 4])
        merged = merge_two_lists(l1, l2)
        assert merge_list_to_values(merged) == [1, 1, 2, 3, 4, 4]

    def test_both_empty(self):
        assert merge_two_lists(None, None) is None

    def test_one_empty(self):
        l2 = build_merge_list([0])
        assert merge_list_to_values(merge_two_lists(None, l2)) == [0]

    def test_disjoint_ranges(self):
        l1 = build_merge_list([1, 2, 3])
        l2 = build_merge_list([4, 5, 6])
        merged = merge_two_lists(l1, l2)
        assert merge_list_to_values(merged) == [1, 2, 3, 4, 5, 6]


class TestLinkedListCycle:
    def test_has_cycle(self):
        head = build_cycle_list([3, 2, 0, -4], cycle_index=1)
        assert has_cycle(head) is True

    def test_no_cycle(self):
        head = build_cycle_list([1, 2, 3], cycle_index=None)
        assert has_cycle(head) is False

    def test_empty(self):
        assert has_cycle(None) is False

    def test_single_node_no_cycle(self):
        head = build_cycle_list([1], cycle_index=None)
        assert has_cycle(head) is False

    def test_single_node_self_cycle(self):
        head = build_cycle_list([1], cycle_index=0)
        assert has_cycle(head) is True


class TestValidateBst:
    def test_valid(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        assert is_valid_bst(root) is True

    def test_invalid_deep_violation(self):
        # 3 sits in the right subtree of 5 but is below 5, which is invalid
        # even though each parent and child pair looks fine locally.
        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        assert is_valid_bst(root) is False

    def test_single_node(self):
        assert is_valid_bst(TreeNode(0)) is True

    def test_empty(self):
        assert is_valid_bst(None) is True

    def test_equal_values_rejected(self):
        # Duplicates break the strict ordering requirement.
        root = TreeNode(2, TreeNode(2))
        assert is_valid_bst(root) is False


class TestCourseSchedule:
    def test_feasible(self):
        assert can_finish(2, [[1, 0]]) is True

    def test_cycle(self):
        assert can_finish(2, [[1, 0], [0, 1]]) is False

    def test_no_prerequisites(self):
        assert can_finish(3, []) is True

    def test_longer_chain(self):
        assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) is True

    def test_self_dependency(self):
        assert can_finish(1, [[0, 0]]) is False


class TestHouseRobber:
    def test_basic(self):
        assert rob([1, 2, 3, 1]) == 4

    def test_alternating(self):
        assert rob([2, 7, 9, 3, 1]) == 12

    def test_single_house(self):
        assert rob([5]) == 5

    def test_empty(self):
        assert rob([]) == 0

    def test_two_houses(self):
        assert rob([2, 1]) == 2


class TestMaximumSubarray:
    def test_basic(self):
        assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_single_element(self):
        assert max_subarray([1]) == 1

    def test_all_negative(self):
        assert max_subarray([-3, -1, -2]) == -1

    def test_all_positive(self):
        assert max_subarray([1, 2, 3, 4]) == 10

    def test_single_negative(self):
        assert max_subarray([-5]) == -5
