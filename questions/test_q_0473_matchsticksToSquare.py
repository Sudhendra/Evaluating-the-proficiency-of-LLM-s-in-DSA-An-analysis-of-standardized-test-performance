import pytest
from q_0473_matchsticksToSquare import Solution


@pytest.mark.parametrize(
    "matchsticks, output", [([1, 1, 2, 2, 2], True), ([3, 3, 3, 3, 4], False)]
)
class TestSolution:
    def test_makesquare(self, matchsticks: List[int], output: bool):
        sc = Solution()
        assert (
            sc.makesquare(
                matchsticks,
            )
            == output
        )
