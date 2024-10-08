import pytest
from q_0141_linkedListCycle import Solution


@pytest.mark.parametrize(
    "head, pos, output", [([3, 2, 0, -4], 1, True), ([1, 2], 0, True), ([1], -1, False)]
)
class TestSolution:
    def test_hasCycle(self, head: Optional[ListNode], output: bool):
        sc = Solution()
        assert (
            sc.hasCycle(
                head,
                pos,
            )
            == output
        )
