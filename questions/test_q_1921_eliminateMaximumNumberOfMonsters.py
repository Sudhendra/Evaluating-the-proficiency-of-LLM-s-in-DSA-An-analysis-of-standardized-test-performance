import pytest
from q_1921_eliminateMaximumNumberOfMonsters import Solution


@pytest.mark.parametrize(
    "dist, speed, output",
    [
        ([1, 3, 4], [1, 1, 1], 3),
        ([1, 1, 2, 3], [1, 1, 1, 1], 1),
        ([3, 2, 4], [5, 3, 2], 1),
    ],
)
class TestSolution:
    def test_eliminateMaximum(self, dist: List[int], speed: List[int], output: int):
        sc = Solution()
        assert (
            sc.eliminateMaximum(
                dist,
                speed,
            )
            == output
        )
