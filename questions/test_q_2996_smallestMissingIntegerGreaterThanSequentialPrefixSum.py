import pytest
from q_2996_smallestMissingIntegerGreaterThanSequentialPrefixSum import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 2, 5], 6), ([3, 4, 5, 1, 12, 14, 13], 15)]
)
class TestSolution:
    def test_missingInteger(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.missingInteger(
                nums,
            )
            == output
        )
