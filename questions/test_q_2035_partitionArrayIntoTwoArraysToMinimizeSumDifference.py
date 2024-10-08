import pytest
from q_2035_partitionArrayIntoTwoArraysToMinimizeSumDifference import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 9, 7, 3], 2), ([-36, 36], 72), ([2, -1, 0, 4, -2, -9], 0)]
)
class TestSolution:
    def test_minimumDifference(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumDifference(
                nums,
            )
            == output
        )
