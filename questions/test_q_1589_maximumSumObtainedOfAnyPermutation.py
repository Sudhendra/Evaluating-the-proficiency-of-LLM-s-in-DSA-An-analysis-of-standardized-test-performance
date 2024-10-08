import pytest
from q_1589_maximumSumObtainedOfAnyPermutation import Solution


@pytest.mark.parametrize(
    "nums, requests, output",
    [
        ([1, 2, 3, 4, 5], [[1, 3], [0, 1]], 19),
        ([1, 2, 3, 4, 5, 6], [[0, 1]], 11),
        ([1, 2, 3, 4, 5, 10], [[0, 2], [1, 3], [1, 1]], 47),
    ],
)
class TestSolution:
    def test_maxSumRangeQuery(
        self, nums: List[int], requests: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.maxSumRangeQuery(
                nums,
                requests,
            )
            == output
        )
