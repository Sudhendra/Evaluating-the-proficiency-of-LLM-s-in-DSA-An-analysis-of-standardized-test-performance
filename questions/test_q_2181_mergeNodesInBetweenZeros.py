import pytest
from q_2181_mergeNodesInBetweenZeros import Solution


@pytest.mark.parametrize(
    "head, output",
    [([0, 3, 1, 0, 4, 5, 2, 0], [4, 11]), ([0, 1, 0, 3, 0, 2, 2, 0], [1, 3, 4])],
)
class TestSolution:
    def test_mergeNodes(self, head: Optional[ListNode], output: Optional[ListNode]):
        sc = Solution()
        assert (
            sc.mergeNodes(
                head,
            )
            == output
        )
