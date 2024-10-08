import pytest
from q_2275_largestCombinationWithBitwiseAndGreaterThanZero import Solution


@pytest.mark.parametrize(
    "candidates, output", [([16, 17, 71, 62, 12, 24, 14], 4), ([8, 8], 2)]
)
class TestSolution:
    def test_largestCombination(self, candidates: List[int], output: int):
        sc = Solution()
        assert (
            sc.largestCombination(
                candidates,
            )
            == output
        )
