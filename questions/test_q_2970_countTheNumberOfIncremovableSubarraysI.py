import pytest
from q_2970_countTheNumberOfIncremovableSubarraysI import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 4], 10), ([6, 5, 7, 8], 7), ([8, 7, 6, 6], 3)]
)
class TestSolution:
    def test_incremovableSubarrayCount(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.incremovableSubarrayCount(
                nums,
            )
            == output
        )
