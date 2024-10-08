import pytest
from q_1785_minimumElementsToAddToFormAGivenSum import Solution


@pytest.mark.parametrize(
    "nums, limit, goal, output", [([1, -1, 1], 3, -4, 2), ([1, -10, 9, 1], 100, 0, 1)]
)
class TestSolution:
    def test_minElements(self, nums: List[int], limit: int, goal: int, output: int):
        sc = Solution()
        assert (
            sc.minElements(
                nums,
                limit,
                goal,
            )
            == output
        )
