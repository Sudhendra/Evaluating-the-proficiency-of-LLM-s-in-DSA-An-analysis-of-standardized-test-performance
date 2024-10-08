import pytest
from q_1674_minimumMovesToMakeArrayComplementary import Solution


@pytest.mark.parametrize(
    "nums, limit, output",
    [([1, 2, 4, 3], 4, 1), ([1, 2, 2, 1], 2, 2), ([1, 2, 1, 2], 2, 0)],
)
class TestSolution:
    def test_minMoves(self, nums: List[int], limit: int, output: int):
        sc = Solution()
        assert (
            sc.minMoves(
                nums,
                limit,
            )
            == output
        )
