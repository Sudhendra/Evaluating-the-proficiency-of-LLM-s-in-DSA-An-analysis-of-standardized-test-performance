import pytest
from q_0021_mergeTwoSortedLists import Solution


@pytest.mark.parametrize(
    "list1, list2, output",
    [([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]), ([], [], []), ([], [0], [0])],
)
class TestSolution:
    def test_mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
        output: Optional[ListNode],
    ):
        sc = Solution()
        assert (
            sc.mergeTwoLists(
                list1,
                list2,
            )
            == output
        )
