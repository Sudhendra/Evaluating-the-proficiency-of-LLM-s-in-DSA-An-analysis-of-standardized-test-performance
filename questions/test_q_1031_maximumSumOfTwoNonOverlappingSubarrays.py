import pytest
from q_1031_maximumSumOfTwoNonOverlappingSubarrays import Solution


@pytest.mark.parametrize(
    "nums, firstLen, secondLen, output",
    [
        ([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2, 20),
        ([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2, 29),
        ([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3, 31),
    ],
)
class TestSolution:
    def test_maxSumTwoNoOverlap(
        self, nums: List[int], firstLen: int, secondLen: int, output: int
    ):
        sc = Solution()
        assert (
            sc.maxSumTwoNoOverlap(
                nums,
                firstLen,
                secondLen,
            )
            == output
        )
