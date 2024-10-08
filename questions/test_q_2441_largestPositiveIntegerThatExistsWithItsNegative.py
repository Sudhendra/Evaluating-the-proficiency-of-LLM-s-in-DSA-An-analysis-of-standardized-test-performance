import pytest
from q_2441_largestPositiveIntegerThatExistsWithItsNegative import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([-1, 2, -3, 3], 3), ([-1, 10, 6, 7, -7, 1], 7), ([-10, 8, 6, 7, -2, -3], -1)],
)
class TestSolution:
    def test_findMaxK(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findMaxK(
                nums,
            )
            == output
        )
