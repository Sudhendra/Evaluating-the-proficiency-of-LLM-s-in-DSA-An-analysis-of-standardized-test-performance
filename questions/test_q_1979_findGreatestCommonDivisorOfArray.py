import pytest
from q_1979_findGreatestCommonDivisorOfArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 5, 6, 9, 10], 2), ([7, 5, 6, 8, 3], 1), ([3, 3], 3)]
)
class TestSolution:
    def test_findGCD(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findGCD(
                nums,
            )
            == output
        )
