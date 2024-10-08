import pytest
from q_0328_oddEvenLinkedList import Solution


@pytest.mark.parametrize(
    "head, output",
    [
        ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
        ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
    ],
)
class TestSolution:
    def test_oddEvenList(self, head: Optional[ListNode], output: Optional[ListNode]):
        sc = Solution()
        assert (
            sc.oddEvenList(
                head,
            )
            == output
        )
