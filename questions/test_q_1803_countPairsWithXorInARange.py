import pytest
from q_1803_countPairsWithXorInARange import Solution


@pytest.mark.parametrize(
    "nums, low, high, output", [([1, 4, 2, 7], 2, 6, 6), ([9, 8, 4, 2, 1], 5, 14, 8)]
)
class TestSolution:
    def test_countPairs(self, nums: List[int], low: int, high: int, output: int):
        sc = Solution()
        assert (
            sc.countPairs(
                nums,
                low,
                high,
            )
            == output
        )
