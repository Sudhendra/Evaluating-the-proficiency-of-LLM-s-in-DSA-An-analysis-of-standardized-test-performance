import pytest
from q_2342_maxSumOfAPairWithEqualSumOfDigits import Solution


@pytest.mark.parametrize(
    "nums, output", [([18, 43, 36, 13, 7], 54), ([10, 12, 19, 14], -1)]
)
class TestSolution:
    def test_maximumSum(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumSum(
                nums,
            )
            == output
        )
