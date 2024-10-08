import pytest
from q_2095_deleteTheMiddleNodeOfALinkedList import Solution


@pytest.mark.parametrize(
    "head, output",
    [
        ([1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]),
        ([1, 2, 3, 4], [1, 2, 4]),
        ([2, 1], [2]),
    ],
)
class TestSolution:
    def test_deleteMiddle(self, head: Optional[ListNode], output: Optional[ListNode]):
        sc = Solution()
        assert (
            sc.deleteMiddle(
                head,
            )
            == output
        )
