import pytest
from q_1027_longestArithmeticSubsequence import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([3, 6, 9, 12], 4), ([9, 4, 7, 2, 10], 3), ([20, 1, 15, 3, 10, 5, 8], 4)],
)
class TestSolution:
    def test_longestArithSeqLength(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.longestArithSeqLength(
                nums,
            )
            == output
        )
