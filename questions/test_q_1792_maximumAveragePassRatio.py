import pytest
from q_1792_maximumAveragePassRatio import Solution


@pytest.mark.parametrize(
    "classes, extraStudents, output",
    [
        ([[1, 2], [3, 5], [2, 2]], 2, 0.78333),
        ([[2, 4], [3, 9], [4, 5], [2, 10]], 4, 0.53485),
    ],
)
class TestSolution:
    def test_maxAverageRatio(
        self, classes: List[List[int]], extraStudents: int, output: float
    ):
        sc = Solution()
        assert (
            sc.maxAverageRatio(
                classes,
                extraStudents,
            )
            == output
        )
