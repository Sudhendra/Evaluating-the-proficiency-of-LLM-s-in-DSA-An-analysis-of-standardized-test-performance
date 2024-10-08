import pytest
from q_0594_longestHarmoniousSubsequence import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 3, 2, 2, 5, 2, 3, 7], 5), ([1, 2, 3, 4], 2), ([1, 1, 1, 1], 0)],
)
class TestSolution:
    def test_findLHS(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findLHS(
                nums,
            )
            == output
        )
