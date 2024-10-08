import pytest
from q_2444_countSubarraysWithFixedBounds import Solution


@pytest.mark.parametrize(
    "nums, minK, maxK, output",
    [([1, 3, 5, 2, 7, 5], 1, 5, 2), ([1, 1, 1, 1], 1, 1, 10)],
)
class TestSolution:
    def test_countSubarrays(self, nums: List[int], minK: int, maxK: int, output: int):
        sc = Solution()
        assert (
            sc.countSubarrays(
                nums,
                minK,
                maxK,
            )
            == output
        )
