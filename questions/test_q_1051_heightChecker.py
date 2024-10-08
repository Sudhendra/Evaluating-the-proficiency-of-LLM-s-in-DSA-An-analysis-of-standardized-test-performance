import pytest
from q_1051_heightChecker import Solution


@pytest.mark.parametrize(
    "heights, output",
    [([1, 1, 4, 2, 1, 3], 3), ([5, 1, 2, 3, 4], 5), ([1, 2, 3, 4, 5], 0)],
)
class TestSolution:
    def test_heightChecker(self, heights: List[int], output: int):
        sc = Solution()
        assert (
            sc.heightChecker(
                heights,
            )
            == output
        )
