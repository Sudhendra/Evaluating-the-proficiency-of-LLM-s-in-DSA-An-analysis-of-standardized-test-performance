import pytest
from q_1007_minimumDominoRotationsForEqualRow import Solution


@pytest.mark.parametrize(
    "tops, bottoms, output",
    [
        ([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2], 2),
        ([3, 5, 1, 2, 3], [3, 6, 3, 3, 4], -1),
    ],
)
class TestSolution:
    def test_minDominoRotations(self, tops: List[int], bottoms: List[int], output: int):
        sc = Solution()
        assert (
            sc.minDominoRotations(
                tops,
                bottoms,
            )
            == output
        )
