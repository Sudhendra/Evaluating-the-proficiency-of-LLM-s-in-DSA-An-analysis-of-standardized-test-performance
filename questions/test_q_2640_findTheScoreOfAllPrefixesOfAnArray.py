import pytest
from q_2640_findTheScoreOfAllPrefixesOfAnArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([2, 3, 7, 5, 10], [4, 10, 24, 36, 56]),
        ([1, 1, 2, 4, 8, 16], [2, 4, 8, 16, 32, 64]),
    ],
)
class TestSolution:
    def test_findPrefixScore(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.findPrefixScore(
                nums,
            )
            == output
        )
