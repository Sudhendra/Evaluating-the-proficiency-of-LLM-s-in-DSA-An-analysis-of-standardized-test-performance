import pytest
from q_0862_shortestSubarrayWithSumAtLeastK import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1], 1, 1), ([1, 2], 4, -1), ([2, -1, 2], 3, 3)]
)
class TestSolution:
    def test_shortestSubarray(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.shortestSubarray(
                nums,
                k,
            )
            == output
        )
