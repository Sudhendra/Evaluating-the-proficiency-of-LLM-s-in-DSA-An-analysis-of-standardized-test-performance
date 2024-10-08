import pytest
from q_2155_allDivisionsWithTheHighestScoreOfABinaryArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([0, 0, 1, 0], [2, 4]), ([0, 0, 0], [3]), ([1, 1], [0])]
)
class TestSolution:
    def test_maxScoreIndices(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.maxScoreIndices(
                nums,
            )
            == output
        )
