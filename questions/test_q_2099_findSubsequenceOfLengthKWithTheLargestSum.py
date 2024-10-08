import pytest
from q_2099_findSubsequenceOfLengthKWithTheLargestSum import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([2, 1, 3, 3], 2, [3, 3]),
        ([-1, -2, 3, 4], 3, [-1, 3, 4]),
        ([3, 4, 3, 3], 2, [3, 4]),
    ],
)
class TestSolution:
    def test_maxSubsequence(self, nums: List[int], k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.maxSubsequence(
                nums,
                k,
            )
            == output
        )
