import pytest
from q_2344_minimumDeletionsToMakeArrayDivisible import Solution


@pytest.mark.parametrize(
    "nums, numsDivide, output",
    [([2, 3, 2, 4, 3], [9, 6, 9, 3, 15], 2), ([4, 3, 6], [8, 2, 6, 10], -1)],
)
class TestSolution:
    def test_minOperations(self, nums: List[int], numsDivide: List[int], output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums,
                numsDivide,
            )
            == output
        )
