import pytest
from q_1171_removeZeroSumConsecutiveNodesFromLinkedList import Solution


@pytest.mark.parametrize(
    "head, output",
    [
        ([1, 2, -3, 3, 1], [3, 1]),
        ([1, 2, 3, -3, 4], [1, 2, 4]),
        ([1, 2, 3, -3, -2], [1]),
    ],
)
class TestSolution:
    def test_removeZeroSumSublists(
        self, head: Optional[ListNode], output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.removeZeroSumSublists(
                head,
            )
            == output
        )
