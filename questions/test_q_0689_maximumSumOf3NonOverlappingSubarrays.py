import pytest
from q_0689_maximumSumOf3NonOverlappingSubarrays import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([1, 2, 1, 2, 6, 7, 5, 1], 2, [0, 3, 5]),
        ([1, 2, 1, 2, 1, 2, 1, 2, 1], 2, [0, 2, 4]),
    ],
)
class TestSolution:
    def test_maxSumOfThreeSubarrays(self, nums: List[int], k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.maxSumOfThreeSubarrays(
                nums,
                k,
            )
            == output
        )
