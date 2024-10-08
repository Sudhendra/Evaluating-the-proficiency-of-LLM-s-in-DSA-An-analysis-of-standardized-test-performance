import pytest
from q_3017_countTheNumberOfHousesAtACertainDistanceIi import Solution


@pytest.mark.parametrize(
    "n, x, y, output",
    [(3, 1, 3, [6, 0, 0]), (5, 2, 4, [10, 8, 2, 0, 0]), (4, 1, 1, [6, 4, 2, 0])],
)
class TestSolution:
    def test_countOfPairs(self, n: int, x: int, y: int, output: List[int]):
        sc = Solution()
        assert (
            sc.countOfPairs(
                n,
                x,
                y,
            )
            == output
        )
