import pytest
from q_2488_countSubarraysWithMedianK import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([3, 2, 1, 4, 5], 4, 3), ([2, 3, 1], 3, 1)]
)
class TestSolution:
    def test_countSubarrays(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.countSubarrays(
                nums,
                k,
            )
            == output
        )
