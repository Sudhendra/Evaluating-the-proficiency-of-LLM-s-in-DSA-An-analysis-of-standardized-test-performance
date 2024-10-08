import pytest
from q_1425_constrainedSubsequenceSum import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([10, 2, -10, 5, 20], 2, 37),
        ([-1, -2, -3], 1, -1),
        ([10, -2, -10, -5, 20], 2, 23),
    ],
)
class TestSolution:
    def test_constrainedSubsetSum(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.constrainedSubsetSum(
                nums,
                k,
            )
            == output
        )
