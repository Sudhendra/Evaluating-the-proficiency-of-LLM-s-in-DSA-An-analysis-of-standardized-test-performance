import pytest
from q_3077_maximumStrengthOfKDisjointSubarrays import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([1, 2, 3, -1, 2], 3, 22), ([12, -2, -2, -2, -2], 5, 64), ([-1, -2, -3], 1, -1)],
)
class TestSolution:
    def test_maximumStrength(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maximumStrength(
                nums,
                k,
            )
            == output
        )
