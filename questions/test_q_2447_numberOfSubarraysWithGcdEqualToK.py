import pytest
from q_2447_numberOfSubarraysWithGcdEqualToK import Solution


@pytest.mark.parametrize("nums, k, output", [([9, 3, 1, 2, 6, 3], 3, 4), ([4], 7, 0)])
class TestSolution:
    def test_subarrayGCD(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.subarrayGCD(
                nums,
                k,
            )
            == output
        )
