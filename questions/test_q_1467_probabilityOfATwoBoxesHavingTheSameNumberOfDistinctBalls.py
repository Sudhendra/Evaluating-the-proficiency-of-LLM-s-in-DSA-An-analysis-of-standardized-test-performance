import pytest
from q_1467_probabilityOfATwoBoxesHavingTheSameNumberOfDistinctBalls import Solution


@pytest.mark.parametrize(
    "balls, output", [([1, 1], 1.0), ([2, 1, 1], 0.66667), ([1, 2, 1, 2], 0.6)]
)
class TestSolution:
    def test_getProbability(self, balls: List[int], output: float):
        sc = Solution()
        assert (
            sc.getProbability(
                balls,
            )
            == output
        )
