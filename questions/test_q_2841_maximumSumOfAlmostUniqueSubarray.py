import pytest
from q_2841_maximumSumOfAlmostUniqueSubarray import Solution


@pytest.mark.parametrize(
    "nums, m, k, output",
    [
        ([2, 6, 7, 3, 1, 7], 3, 4, 18),
        ([5, 9, 9, 2, 4, 5, 4], 1, 3, 23),
        ([1, 2, 1, 2, 1, 2, 1], 3, 3, 0),
    ],
)
class TestSolution:
    def test_maxSum(self, nums: List[int], m: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.maxSum(
                nums,
                m,
                k,
            )
            == output
        )
