import pytest
from q_0643_maximumAverageSubarrayI import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 12, -5, -6, 50, 3], 4, 12.75), ([5], 1, 5.0)]
)
class TestSolution:
    def test_findMaxAverage(self, nums: List[int], k: int, output: float):
        sc = Solution()
        assert (
            sc.findMaxAverage(
                nums,
                k,
            )
            == output
        )
