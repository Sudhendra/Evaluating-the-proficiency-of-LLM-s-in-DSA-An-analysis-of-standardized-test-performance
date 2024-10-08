import pytest
from q_1498_numberOfSubsequencesThatSatisfyTheGivenSumCondition import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [([3, 5, 6, 7], 9, 4), ([3, 3, 6, 8], 10, 6), ([2, 3, 3, 4, 6, 7], 12, 61)],
)
class TestSolution:
    def test_numSubseq(self, nums: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.numSubseq(
                nums,
                target,
            )
            == output
        )
