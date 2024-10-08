import pytest
from q_0092_reverseLinkedListIi import Solution


@pytest.mark.parametrize(
    "head, left, right, output",
    [([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]), ([5], 1, 1, [5])],
)
class TestSolution:
    def test_reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int,
        output: Optional[ListNode],
    ):
        sc = Solution()
        assert (
            sc.reverseBetween(
                head,
                left,
                right,
            )
            == output
        )
