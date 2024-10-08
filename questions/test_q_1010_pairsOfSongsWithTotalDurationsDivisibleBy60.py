import pytest
from q_1010_pairsOfSongsWithTotalDurationsDivisibleBy60 import Solution


@pytest.mark.parametrize(
    "time, output", [([30, 20, 150, 100, 40], 3), ([60, 60, 60], 3)]
)
class TestSolution:
    def test_numPairsDivisibleBy60(self, time: List[int], output: int):
        sc = Solution()
        assert (
            sc.numPairsDivisibleBy60(
                time,
            )
            == output
        )
