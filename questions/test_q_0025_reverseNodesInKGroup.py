import pytest
from q_0025_reverseNodesInKGroup import Solution


@pytest.mark.parametrize(
    "head, k, output",
    [([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]), ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5])],
)
class TestSolution:
    def test_reverseKGroup(
        self, head: Optional[ListNode], k: int, output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.reverseKGroup(
                head,
                k,
            )
            == output
        )
