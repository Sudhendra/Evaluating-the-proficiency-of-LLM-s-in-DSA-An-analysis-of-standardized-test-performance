import pytest
from q_0143_reorderList import Solution


@pytest.mark.parametrize(
    "head, output", [([1, 2, 3, 4], [1, 4, 2, 3]), ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3])]
)
class TestSolution:
    def test_reorderList(self, head: Optional[ListNode], output: None):
        sc = Solution()
        assert (
            sc.reorderList(
                head,
            )
            == output
        )
