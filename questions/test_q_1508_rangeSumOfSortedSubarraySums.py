import pytest
from q_1508_rangeSumOfSortedSubarraySums import Solution


@pytest.mark.parametrize(
    "nums, n, left, right, output",
    [
        ([1, 2, 3, 4], 4, 1, 5, 13),
        ([1, 2, 3, 4], 4, 3, 4, 6),
        ([1, 2, 3, 4], 4, 1, 10, 50),
    ],
)
class TestSolution:
    def test_rangeSum(
        self, nums: List[int], n: int, left: int, right: int, output: int
    ):
        sc = Solution()
        assert (
            sc.rangeSum(
                nums,
                n,
                left,
                right,
            )
            == output
        )
