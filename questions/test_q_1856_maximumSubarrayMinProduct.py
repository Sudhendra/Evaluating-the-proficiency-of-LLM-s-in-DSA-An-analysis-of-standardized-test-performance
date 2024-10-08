import pytest
from q_1856_maximumSubarrayMinProduct import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 3, 2], 14), ([2, 3, 3, 1, 2], 18), ([3, 1, 5, 6, 4, 2], 60)],
)
class TestSolution:
    def test_maxSumMinProduct(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxSumMinProduct(
                nums,
            )
            == output
        )
