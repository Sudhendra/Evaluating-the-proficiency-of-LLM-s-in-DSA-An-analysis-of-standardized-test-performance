import pytest
from q_1799_maximizeScoreAfterNOperations import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2], 1), ([3, 4, 6, 8], 11), ([1, 2, 3, 4, 5, 6], 14)]
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
