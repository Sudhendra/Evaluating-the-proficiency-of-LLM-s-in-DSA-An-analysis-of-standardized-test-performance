import pytest
from q_2373_largestLocalValuesInAMatrix import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]], [[9, 9], [8, 6]]),
        (
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 2, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ],
            [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
        ),
    ],
)
class TestSolution:
    def test_largestLocal(self, grid: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.largestLocal(
                grid,
            )
            == output
        )
