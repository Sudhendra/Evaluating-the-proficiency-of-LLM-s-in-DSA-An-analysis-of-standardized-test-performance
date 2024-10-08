import pytest
from q_1042_flowerPlantingWithNoAdjacent import Solution


@pytest.mark.parametrize(
    "n, paths, output",
    [
        (3, [[1, 2], [2, 3], [3, 1]], [1, 2, 3]),
        (4, [[1, 2], [3, 4]], [1, 2, 1, 2]),
        (4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]], [1, 2, 3, 4]),
    ],
)
class TestSolution:
    def test_gardenNoAdj(self, n: int, paths: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.gardenNoAdj(
                n,
                paths,
            )
            == output
        )
