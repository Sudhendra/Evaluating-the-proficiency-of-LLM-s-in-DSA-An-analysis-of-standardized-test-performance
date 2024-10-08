import pytest
from q_2598_smallestMissingNonNegativeIntegerAfterOperations import Solution


@pytest.mark.parametrize(
    "nums, value, output",
    [([1, -10, 7, 13, 6, 8], 5, 4), ([1, -10, 7, 13, 6, 8], 7, 2)],
)
class TestSolution:
    def test_findSmallestInteger(self, nums: List[int], value: int, output: int):
        sc = Solution()
        assert (
            sc.findSmallestInteger(
                nums,
                value,
            )
            == output
        )
