import pytest
from q_2074_reverseNodesInEvenLengthGroups import Solution


@pytest.mark.parametrize(
    "head, output",
    [
        ([5, 2, 6, 3, 9, 1, 7, 3, 8, 4], [5, 6, 2, 3, 9, 1, 4, 8, 3, 7]),
        ([1, 1, 0, 6], [1, 0, 1, 6]),
        ([1, 1, 0, 6, 5], [1, 0, 1, 5, 6]),
    ],
)
class TestSolution:
    def test_reverseEvenLengthGroups(
        self, head: Optional[ListNode], output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.reverseEvenLengthGroups(
                head,
            )
            == output
        )
