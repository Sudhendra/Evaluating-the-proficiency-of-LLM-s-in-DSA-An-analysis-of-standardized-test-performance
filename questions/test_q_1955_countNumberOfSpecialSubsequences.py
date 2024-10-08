import pytest
from q_1955_countNumberOfSpecialSubsequences import Solution


@pytest.mark.parametrize(
    "nums, output", [([0, 1, 2, 2], 3), ([2, 2, 0, 0], 0), ([0, 1, 2, 0, 1, 2], 7)]
)
class TestSolution:
    def test_countSpecialSubsequences(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countSpecialSubsequences(
                nums,
            )
            == output
        )
