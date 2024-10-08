import pytest
from q_2709_greatestCommonDivisorTraversal import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 3, 6], True), ([3, 9, 5], False), ([4, 3, 12, 8], True)]
)
class TestSolution:
    def test_canTraverseAllPairs(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.canTraverseAllPairs(
                nums,
            )
            == output
        )
