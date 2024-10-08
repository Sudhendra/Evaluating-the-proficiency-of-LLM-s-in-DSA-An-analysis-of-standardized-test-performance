import pytest
from q_1283_findTheSmallestDivisorGivenAThreshold import Solution


@pytest.mark.parametrize(
    "nums, threshold, output", [([1, 2, 5, 9], 6, 5), ([44, 22, 33, 11, 1], 5, 44)]
)
class TestSolution:
    def test_smallestDivisor(self, nums: List[int], threshold: int, output: int):
        sc = Solution()
        assert (
            sc.smallestDivisor(
                nums,
                threshold,
            )
            == output
        )
