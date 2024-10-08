import pytest
from q_0446_arithmeticSlicesIiSubsequence import Solution


@pytest.mark.parametrize("nums, output", [([2, 4, 6, 8, 10], 7), ([7, 7, 7, 7, 7], 16)])
class TestSolution:
    def test_numberOfArithmeticSlices(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.numberOfArithmeticSlices(
                nums,
            )
            == output
        )
