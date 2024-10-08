import pytest
from q_1742_maximumNumberOfBallsInABox import Solution


@pytest.mark.parametrize(
    "lowLimit, highLimit, output", [(1, 10, 2), (5, 15, 2), (19, 28, 2)]
)
class TestSolution:
    def test_countBalls(self, lowLimit: int, highLimit: int, output: int):
        sc = Solution()
        assert (
            sc.countBalls(
                lowLimit,
                highLimit,
            )
            == output
        )
