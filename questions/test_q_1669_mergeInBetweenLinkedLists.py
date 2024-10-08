import pytest
from q_1669_mergeInBetweenLinkedLists import Solution


@pytest.mark.parametrize(
    "list1, a, b, list2, output",
    [
        (
            [10, 1, 13, 6, 9, 5],
            3,
            4,
            [1000000, 1000001, 1000002],
            [10, 1, 13, 1000000, 1000001, 1000002, 5],
        ),
        (
            [0, 1, 2, 3, 4, 5, 6],
            2,
            5,
            [1000000, 1000001, 1000002, 1000003, 1000004],
            [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6],
        ),
    ],
)
class TestSolution:
    def test_mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode, output: ListNode
    ):
        sc = Solution()
        assert (
            sc.mergeInBetween(
                list1,
                a,
                b,
                list2,
            )
            == output
        )
