import pytest
from q_0891_sumOfSubsequenceWidths import Solution


@pytest.mark.parametrize("nums, output", [([2, 1, 3], 6), ([2], 0)])
class TestSolution:
    def test_sumSubseqWidths(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.sumSubseqWidths(
                nums,
            )
            == output
        )
