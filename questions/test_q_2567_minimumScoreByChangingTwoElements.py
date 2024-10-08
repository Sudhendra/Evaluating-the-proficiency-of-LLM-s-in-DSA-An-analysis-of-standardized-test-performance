import pytest
from q_2567_minimumScoreByChangingTwoElements import Solution


@pytest.mark.parametrize("nums, output", [([1, 4, 3], 0), ([1, 4, 7, 8, 5], 3)])
class TestSolution:
    def test_minimizeSum(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimizeSum(
                nums,
            )
            == output
        )
