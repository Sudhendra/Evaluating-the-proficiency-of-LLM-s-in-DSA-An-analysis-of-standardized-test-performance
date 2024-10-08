import pytest
from q_2593_findScoreOfAnArrayAfterMarkingAllElements import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 1, 3, 4, 5, 2], 7), ([2, 3, 5, 1, 3, 2], 5)]
)
class TestSolution:
    def test_findScore(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findScore(
                nums,
            )
            == output
        )
