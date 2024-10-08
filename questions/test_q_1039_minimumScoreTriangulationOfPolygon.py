import pytest
from q_1039_minimumScoreTriangulationOfPolygon import Solution


@pytest.mark.parametrize(
    "values, output", [([1, 2, 3], 6), ([3, 7, 4, 5], 144), ([1, 3, 1, 4, 1, 5], 13)]
)
class TestSolution:
    def test_minScoreTriangulation(self, values: List[int], output: int):
        sc = Solution()
        assert (
            sc.minScoreTriangulation(
                values,
            )
            == output
        )
