import pytest
from q_2006_countNumberOfPairsWithAbsoluteDifferenceK import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 2, 2, 1], 1, 4), ([1, 3], 3, 0), ([3, 2, 1, 5, 4], 2, 3)]
)
class TestSolution:
    def test_countKDifference(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.countKDifference(
                nums,
                k,
            )
            == output
        )
