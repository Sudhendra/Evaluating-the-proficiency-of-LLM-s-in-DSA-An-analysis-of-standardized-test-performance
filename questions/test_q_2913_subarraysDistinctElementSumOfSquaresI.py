import pytest
from q_2913_subarraysDistinctElementSumOfSquaresI import Solution


@pytest.mark.parametrize("nums, output", [([1, 2, 1], 15), ([1, 1], 3)])
class TestSolution:
    def test_sumCounts(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.sumCounts(
                nums,
            )
            == output
        )
