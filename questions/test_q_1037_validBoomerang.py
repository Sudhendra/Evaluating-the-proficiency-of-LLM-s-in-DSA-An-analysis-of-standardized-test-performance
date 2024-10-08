import pytest
from q_1037_validBoomerang import Solution


@pytest.mark.parametrize(
    "points, output",
    [([[1, 1], [2, 3], [3, 2]], True), ([[1, 1], [2, 2], [3, 3]], False)],
)
class TestSolution:
    def test_isBoomerang(self, points: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.isBoomerang(
                points,
            )
            == output
        )
