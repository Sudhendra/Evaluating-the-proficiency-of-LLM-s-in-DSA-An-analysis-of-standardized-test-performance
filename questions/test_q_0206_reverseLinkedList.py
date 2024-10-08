import pytest
from q_0206_reverseLinkedList import Solution


@pytest.mark.parametrize(
    "head, output", [([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), ([1, 2], [2, 1]), ([], [])]
)
class TestSolution:
    def test_reverseList(self, head: Optional[ListNode], output: Optional[ListNode]):
        sc = Solution()
        assert (
            sc.reverseList(
                head,
            )
            == output
        )
