import pytest
from q_0147_insertionSortList import Solution


@pytest.mark.parametrize(
    "head, output", [([4, 2, 1, 3], [1, 2, 3, 4]), ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5])]
)
class TestSolution:
    def test_insertionSortList(
        self, head: Optional[ListNode], output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.insertionSortList(
                head,
            )
            == output
        )
