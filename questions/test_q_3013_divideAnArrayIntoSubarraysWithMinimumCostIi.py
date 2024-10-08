import pytest
from q_3013_divideAnArrayIntoSubarraysWithMinimumCostIi import Solution


@pytest.mark.parametrize(
    "nums, k, dist, output",
    [
        ([1, 3, 2, 6, 4, 2], 3, 3, 5),
        ([10, 1, 2, 2, 2, 1], 4, 3, 15),
        ([10, 8, 18, 9], 3, 1, 36),
    ],
)
class TestSolution:
    def test_minimumCost(self, nums: List[int], k: int, dist: int, output: int):
        sc = Solution()
        assert (
            sc.minimumCost(
                nums,
                k,
                dist,
            )
            == output
        )
