import pytest
from q_0023_mergeKSortedLists import Solution


@pytest.mark.parametrize(
    "lists, output",
    [([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]), ([], []), ([[]], [])],
)
class TestSolution:
    def test_mergeKLists(
        self, lists: List[Optional[ListNode]], output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.mergeKLists(
                lists,
            )
            == output
        )
