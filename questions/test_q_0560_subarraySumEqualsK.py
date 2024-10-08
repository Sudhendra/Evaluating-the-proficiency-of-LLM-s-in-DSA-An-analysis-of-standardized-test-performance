import pytest
from q_0560_subarraySumEqualsK import Solution


@pytest.mark.parametrize("nums, k, output", [([1, 1, 1], 2, 2), ([1, 2, 3], 3, 2)])
class TestSolution:
    def test_subarraySum(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.subarraySum(
                nums,
                k,
            )
            == output
        )
