import pytest
from q_2866_beautifulTowersIi import Solution


@pytest.mark.parametrize(
    "maxHeights, output",
    [([5, 3, 4, 1, 1], 13), ([6, 5, 3, 9, 2, 7], 22), ([3, 2, 5, 5, 2, 3], 18)],
)
class TestSolution:
    def test_maximumSumOfHeights(self, maxHeights: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumSumOfHeights(
                maxHeights,
            )
            == output
        )
