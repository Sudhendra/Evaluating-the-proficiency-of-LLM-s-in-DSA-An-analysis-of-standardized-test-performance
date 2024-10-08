import pytest
from q_2644_findTheMaximumDivisibilityScore import Solution


@pytest.mark.parametrize(
    "nums, divisors, output",
    [
        ([4, 7, 9, 3, 9], [5, 2, 3], 3),
        ([20, 14, 21, 10], [5, 7, 5], 5),
        ([12], [10, 16], 10),
    ],
)
class TestSolution:
    def test_maxDivScore(self, nums: List[int], divisors: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxDivScore(
                nums,
                divisors,
            )
            == output
        )
