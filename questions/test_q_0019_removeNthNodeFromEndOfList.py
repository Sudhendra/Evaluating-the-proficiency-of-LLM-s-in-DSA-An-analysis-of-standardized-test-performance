import pytest
from q_0019_removeNthNodeFromEndOfList import Solution


@pytest.mark.parametrize(
    "head, n, output",
    [([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]), ([1], 1, []), ([1, 2], 1, [1])],
)
class TestSolution:
    def test_removeNthFromEnd(
        self, head: Optional[ListNode], n: int, output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.removeNthFromEnd(
                head,
                n,
            )
            == output
        )
