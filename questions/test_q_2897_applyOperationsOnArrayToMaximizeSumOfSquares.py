import pytest
from q_2897_applyOperationsOnArrayToMaximizeSumOfSquares import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([2, 6, 5, 8], 2, 261), ([4, 5, 4, 7], 3, 90)]
)
class TestSolution:
    def test_maxSum(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maxSum(
                nums,
                k,
            )
            == output
        )
