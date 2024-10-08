import pytest
from q_2654_minimumNumberOfOperationsToMakeAllArrayElementsEqualTo1 import Solution


@pytest.mark.parametrize("nums, output", [([2, 6, 3, 4], 4), ([2, 10, 6, 14], -1)])
class TestSolution:
    def test_minOperations(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums,
            )
            == output
        )
