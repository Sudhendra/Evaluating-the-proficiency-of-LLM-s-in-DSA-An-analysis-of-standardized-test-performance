import pytest
from q_2302_countSubarraysWithScoreLessThanK import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([2, 1, 4, 3, 5], 10, 6), ([1, 1, 1], 5, 5)]
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
