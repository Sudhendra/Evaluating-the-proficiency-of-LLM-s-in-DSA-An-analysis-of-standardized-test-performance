import pytest
from q_2470_numberOfSubarraysWithLcmEqualToK import Solution


@pytest.mark.parametrize("nums, k, output", [([3, 6, 2, 7, 1], 6, 4), ([3], 2, 0)])
class TestSolution:
    def test_subarrayLCM(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.subarrayLCM(
                nums,
                k,
            )
            == output
        )
