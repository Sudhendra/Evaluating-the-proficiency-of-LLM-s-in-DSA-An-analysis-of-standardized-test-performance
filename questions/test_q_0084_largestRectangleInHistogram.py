import pytest
from q_0084_largestRectangleInHistogram import Solution


@pytest.mark.parametrize("heights, output", [([2, 1, 5, 6, 2, 3], 10), ([2, 4], 4)])
class TestSolution:
    def test_largestRectangleArea(self, heights: List[int], output: int):
        sc = Solution()
        assert (
            sc.largestRectangleArea(
                heights,
            )
            == output
        )
