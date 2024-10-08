import pytest
from q_1509_minimumDifferenceBetweenLargestAndSmallestValueInThreeMoves import Solution


@pytest.mark.parametrize(
    "nums, output", [([5, 3, 2, 4], 0), ([1, 5, 0, 10, 14], 1), ([3, 100, 20], 0)]
)
class TestSolution:
    def test_minDifference(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minDifference(
                nums,
            )
            == output
        )
