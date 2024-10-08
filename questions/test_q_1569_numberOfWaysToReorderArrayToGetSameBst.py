import pytest
from q_1569_numberOfWaysToReorderArrayToGetSameBst import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 1, 3], 1), ([3, 4, 5, 1, 2], 5), ([1, 2, 3], 0)]
)
class TestSolution:
    def test_numOfWays(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.numOfWays(
                nums,
            )
            == output
        )
