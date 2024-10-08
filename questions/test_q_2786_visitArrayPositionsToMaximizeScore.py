import pytest
from q_2786_visitArrayPositionsToMaximizeScore import Solution


@pytest.mark.parametrize(
    "nums, x, output", [([2, 3, 6, 1, 9, 2], 5, 13), ([2, 4, 6, 8], 3, 20)]
)
class TestSolution:
    def test_maxScore(self, nums: List[int], x: int, output: int):
        sc = Solution()
        assert (
            sc.maxScore(
                nums,
                x,
            )
            == output
        )
