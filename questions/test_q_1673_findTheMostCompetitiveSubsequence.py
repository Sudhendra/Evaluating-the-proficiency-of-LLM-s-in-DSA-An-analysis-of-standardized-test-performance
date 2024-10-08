import pytest
from q_1673_findTheMostCompetitiveSubsequence import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([3, 5, 2, 6], 2, [2, 6]), ([2, 4, 3, 3, 5, 4, 9, 6], 4, [2, 3, 3, 4])],
)
class TestSolution:
    def test_mostCompetitive(self, nums: List[int], k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.mostCompetitive(
                nums,
                k,
            )
            == output
        )
