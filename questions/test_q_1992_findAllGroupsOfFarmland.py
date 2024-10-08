import pytest
from q_1992_findAllGroupsOfFarmland import Solution


@pytest.mark.parametrize(
    "land, output",
    [
        ([[1, 0, 0], [0, 1, 1], [0, 1, 1]], [[0, 0, 0, 0], [1, 1, 2, 2]]),
        ([[1, 1], [1, 1]], [[0, 0, 1, 1]]),
        ([[0]], []),
    ],
)
class TestSolution:
    def test_findFarmland(self, land: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.findFarmland(
                land,
            )
            == output
        )
