import pytest
from q_2817_minimumAbsoluteDifferenceBetweenElementsWithConstraint import Solution


@pytest.mark.parametrize(
    "nums, x, output",
    [([4, 3, 2, 4], 2, 0), ([5, 3, 2, 10, 15], 1, 1), ([1, 2, 3, 4], 3, 3)],
)
class TestSolution:
    def test_minAbsoluteDifference(self, nums: List[int], x: int, output: int):
        sc = Solution()
        assert (
            sc.minAbsoluteDifference(
                nums,
                x,
            )
            == output
        )
