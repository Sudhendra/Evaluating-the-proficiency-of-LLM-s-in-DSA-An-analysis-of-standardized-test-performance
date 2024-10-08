import pytest
from q_2442_countNumberOfDistinctIntegersAfterReverseOperations import Solution


@pytest.mark.parametrize("nums, output", [([1, 13, 10, 12, 31], 6), ([2, 2, 2], 1)])
class TestSolution:
    def test_countDistinctIntegers(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countDistinctIntegers(
                nums,
            )
            == output
        )
