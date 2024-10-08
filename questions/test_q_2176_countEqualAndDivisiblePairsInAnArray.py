import pytest
from q_2176_countEqualAndDivisiblePairsInAnArray import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([3, 1, 2, 2, 2, 1, 3], 2, 4), ([1, 2, 3, 4], 1, 0)]
)
class TestSolution:
    def test_countPairs(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.countPairs(
                nums,
                k,
            )
            == output
        )
