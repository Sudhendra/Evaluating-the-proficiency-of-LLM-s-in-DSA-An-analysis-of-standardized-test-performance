import pytest
from q_0646_maximumLengthOfPairChain import Solution


@pytest.mark.parametrize(
    "pairs, output", [([[1, 2], [2, 3], [3, 4]], 2), ([[1, 2], [7, 8], [4, 5]], 3)]
)
class TestSolution:
    def test_findLongestChain(self, pairs: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.findLongestChain(
                pairs,
            )
            == output
        )
