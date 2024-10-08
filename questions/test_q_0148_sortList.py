import pytest
from q_0148_sortList import Solution


@pytest.mark.parametrize(
    "head, output",
    [([4, 2, 1, 3], [1, 2, 3, 4]), ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]), ([], [])],
)
class TestSolution:
    def test_sortList(self, head: Optional[ListNode], output: Optional[ListNode]):
        sc = Solution()
        assert (
            sc.sortList(
                head,
            )
            == output
        )
