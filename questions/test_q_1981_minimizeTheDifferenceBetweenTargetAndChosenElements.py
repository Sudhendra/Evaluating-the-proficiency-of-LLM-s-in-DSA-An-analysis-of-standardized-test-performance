import pytest
from q_1981_minimizeTheDifferenceBetweenTargetAndChosenElements import Solution


@pytest.mark.parametrize(
    "mat, target, output",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13, 0),
        ([[1], [2], [3]], 100, 94),
        ([[1, 2, 9, 8, 7]], 6, 1),
    ],
)
class TestSolution:
    def test_minimizeTheDifference(
        self, mat: List[List[int]], target: int, output: int
    ):
        sc = Solution()
        assert (
            sc.minimizeTheDifference(
                mat,
                target,
            )
            == output
        )
