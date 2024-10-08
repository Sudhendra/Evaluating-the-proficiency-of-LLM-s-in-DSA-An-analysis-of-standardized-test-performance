import pytest
from q_0082_removeDuplicatesFromSortedListIi import Solution


@pytest.mark.parametrize(
    "head, output", [([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]), ([1, 1, 1, 2, 3], [2, 3])]
)
class TestSolution:
    def test_deleteDuplicates(
        self, head: Optional[ListNode], output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.deleteDuplicates(
                head,
            )
            == output
        )
