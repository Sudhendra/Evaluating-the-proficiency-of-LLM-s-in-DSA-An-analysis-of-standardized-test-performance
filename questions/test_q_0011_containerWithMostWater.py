import pytest
from q_0011_containerWithMostWater import Solution


@pytest.mark.parametrize(
    "height, output", [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1)]
)
class TestSolution:
    def test_maxArea(self, height: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxArea(
                height,
            )
            == output
        )
