import pytest
from q_2762_continuousSubarrays import Solution


@pytest.mark.parametrize("nums, output", [([5, 4, 2, 4], 8), ([1, 2, 3], 6)])
class TestSolution:
    def test_continuousSubarrays(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.continuousSubarrays(
                nums,
            )
            == output
        )
