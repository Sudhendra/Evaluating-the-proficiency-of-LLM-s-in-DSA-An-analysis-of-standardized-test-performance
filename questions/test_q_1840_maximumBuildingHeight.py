import pytest
from q_1840_maximumBuildingHeight import Solution


@pytest.mark.parametrize(
    "n, restrictions, output",
    [(5, [[2, 1], [4, 1]], 2), (6, [], 5), (10, [[5, 3], [2, 5], [7, 4], [10, 3]], 5)],
)
class TestSolution:
    def test_maxBuilding(self, n: int, restrictions: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxBuilding(
                n,
                restrictions,
            )
            == output
        )
