import pytest
from q_1558_minimumNumbersOfFunctionCallsToMakeTargetArray import Solution


@pytest.mark.parametrize("nums, output", [([1, 5], 5), ([2, 2], 3), ([4, 2, 5], 6)])
class TestSolution:
    def test_minOperations(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums,
            )
            == output
        )
