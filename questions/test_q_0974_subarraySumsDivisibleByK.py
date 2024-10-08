import pytest
from q_0974_subarraySumsDivisibleByK import Solution


@pytest.mark.parametrize("nums, k, output", [([4, 5, 0, -2, -3, 1], 5, 7), ([5], 9, 0)])
class TestSolution:
    def test_subarraysDivByK(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.subarraysDivByK(
                nums,
                k,
            )
            == output
        )
