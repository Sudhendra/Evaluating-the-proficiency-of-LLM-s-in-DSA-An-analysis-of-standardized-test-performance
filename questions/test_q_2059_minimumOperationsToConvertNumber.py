import pytest
from q_2059_minimumOperationsToConvertNumber import Solution


@pytest.mark.parametrize(
    "nums, start, goal, output",
    [([2, 4, 12], 2, 12, 2), ([3, 5, 7], 0, -4, 2), ([2, 8, 16], 0, 1, -1)],
)
class TestSolution:
    def test_minimumOperations(
        self, nums: List[int], start: int, goal: int, output: int
    ):
        sc = Solution()
        assert (
            sc.minimumOperations(
                nums,
                start,
                goal,
            )
            == output
        )
