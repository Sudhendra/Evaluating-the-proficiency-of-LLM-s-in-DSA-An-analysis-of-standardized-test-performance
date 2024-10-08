import pytest
from q_2916_subarraysDistinctElementSumOfSquaresIi import Solution


@pytest.mark.parametrize("nums, output", [([1, 2, 1], 15), ([2, 2], 3)])
class TestSolution:
    def test_sumCounts(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.sumCounts(
                nums,
            )
            == output
        )
