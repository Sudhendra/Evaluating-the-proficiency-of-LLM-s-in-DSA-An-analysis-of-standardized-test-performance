import pytest
from q_1911_maximumAlternatingSubsequenceSum import Solution


@pytest.mark.parametrize(
    "nums, output", [([4, 2, 5, 3], 7), ([5, 6, 7, 8], 8), ([6, 2, 1, 2, 4, 5], 10)]
)
class TestSolution:
    def test_maxAlternatingSum(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxAlternatingSum(
                nums,
            )
            == output
        )
