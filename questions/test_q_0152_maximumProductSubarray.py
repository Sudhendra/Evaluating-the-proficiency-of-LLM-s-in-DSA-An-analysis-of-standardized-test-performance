import pytest
from q_0152_maximumProductSubarray import Solution


@pytest.mark.parametrize("nums, output", [([2, 3, -2, 4], 6), ([-2, 0, -1], 0)])
class TestSolution:
    def test_maxProduct(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxProduct(
                nums,
            )
            == output
        )
