import pytest
from q_0407_trappingRainWaterIi import Solution


@pytest.mark.parametrize(
    "heightMap, output",
    [
        ([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]], 4),
        (
            [
                [3, 3, 3, 3, 3],
                [3, 2, 2, 2, 3],
                [3, 2, 1, 2, 3],
                [3, 2, 2, 2, 3],
                [3, 3, 3, 3, 3],
            ],
            10,
        ),
    ],
)
class TestSolution:
    def test_trapRainWater(self, heightMap: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.trapRainWater(
                heightMap,
            )
            == output
        )
