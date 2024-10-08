import pytest
from q_2382_maximumSegmentSumAfterRemovals import Solution


@pytest.mark.parametrize(
    "nums, removeQueries, output",
    [
        ([1, 2, 5, 6, 1], [0, 3, 2, 4, 1], [14, 7, 2, 2, 0]),
        ([3, 2, 11, 1], [3, 2, 1, 0], [16, 5, 3, 0]),
    ],
)
class TestSolution:
    def test_maximumSegmentSum(
        self, nums: List[int], removeQueries: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.maximumSegmentSum(
                nums,
                removeQueries,
            )
            == output
        )
