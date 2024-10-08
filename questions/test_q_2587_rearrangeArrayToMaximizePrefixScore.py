import pytest
from q_2587_rearrangeArrayToMaximizePrefixScore import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, -1, 0, 1, -3, 3, -3], 6), ([-2, -3, 0], 0)]
)
class TestSolution:
    def test_maxScore(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxScore(
                nums,
            )
            == output
        )
