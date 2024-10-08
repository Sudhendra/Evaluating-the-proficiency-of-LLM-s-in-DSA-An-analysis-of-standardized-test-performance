import pytest
from q_0719_findKThSmallestPairDistance import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 3, 1], 1, 0), ([1, 1, 1], 2, 0), ([1, 6, 1], 3, 5)]
)
class TestSolution:
    def test_smallestDistancePair(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.smallestDistancePair(
                nums,
                k,
            )
            == output
        )
