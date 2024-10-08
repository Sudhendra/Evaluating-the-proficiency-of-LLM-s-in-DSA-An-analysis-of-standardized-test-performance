import pytest
from q_3066_minimumOperationsToExceedThresholdValueIi import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([2, 11, 10, 1, 3], 10, 2), ([1, 1, 2, 4, 9], 20, 4)]
)
class TestSolution:
    def test_minOperations(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums,
                k,
            )
            == output
        )
