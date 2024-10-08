import pytest
from q_1005_maximizeSumOfArrayAfterKNegations import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([4, 2, 3], 1, 5), ([3, -1, 0, 2], 3, 6), ([2, -3, -1, 5, -4], 2, 13)],
)
class TestSolution:
    def test_largestSumAfterKNegations(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.largestSumAfterKNegations(
                nums,
                k,
            )
            == output
        )
