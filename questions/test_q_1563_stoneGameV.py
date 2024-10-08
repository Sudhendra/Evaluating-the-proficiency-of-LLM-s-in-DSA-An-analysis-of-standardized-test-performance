import pytest
from q_1563_stoneGameV import Solution


@pytest.mark.parametrize(
    "stoneValue, output",
    [([6, 2, 3, 4, 5, 5], 18), ([7, 7, 7, 7, 7, 7, 7], 28), ([4], 0)],
)
class TestSolution:
    def test_stoneGameV(self, stoneValue: List[int], output: int):
        sc = Solution()
        assert (
            sc.stoneGameV(
                stoneValue,
            )
            == output
        )
