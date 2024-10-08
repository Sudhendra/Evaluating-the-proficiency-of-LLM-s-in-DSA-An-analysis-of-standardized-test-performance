import pytest
from q_2824_countPairsWhoseSumIsLessThanTarget import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [([-1, 1, 2, 3, 1], 2, 3), ([-6, 2, 5, -2, -7, -1, 3], -2, 10)],
)
class TestSolution:
    def test_countPairs(self, nums: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.countPairs(
                nums,
                target,
            )
            == output
        )
