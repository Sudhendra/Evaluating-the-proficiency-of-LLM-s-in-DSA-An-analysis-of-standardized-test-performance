import pytest
from q_1403_minimumSubsequenceInNonIncreasingOrder import Solution


@pytest.mark.parametrize(
    "nums, output", [([4, 3, 10, 9, 8], [10, 9]), ([4, 4, 7, 6, 7], [7, 7, 6])]
)
class TestSolution:
    def test_minSubsequence(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.minSubsequence(
                nums,
            )
            == output
        )
