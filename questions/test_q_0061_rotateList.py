import pytest
from q_0061_rotateList import Solution


@pytest.mark.parametrize(
    "head, k, output",
    [([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]), ([0, 1, 2], 4, [2, 0, 1])],
)
class TestSolution:
    def test_rotateRight(
        self, head: Optional[ListNode], k: int, output: Optional[ListNode]
    ):
        sc = Solution()
        assert (
            sc.rotateRight(
                head,
                k,
            )
            == output
        )
