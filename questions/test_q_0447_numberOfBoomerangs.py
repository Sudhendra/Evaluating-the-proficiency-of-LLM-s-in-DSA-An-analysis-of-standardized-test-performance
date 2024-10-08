import pytest
from q_0447_numberOfBoomerangs import Solution


@pytest.mark.parametrize(
    "points, output",
    [([[0, 0], [1, 0], [2, 0]], 2), ([[1, 1], [2, 2], [3, 3]], 2), ([[1, 1]], 0)],
)
class TestSolution:
    def test_numberOfBoomerangs(self, points: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.numberOfBoomerangs(
                points,
            )
            == output
        )
