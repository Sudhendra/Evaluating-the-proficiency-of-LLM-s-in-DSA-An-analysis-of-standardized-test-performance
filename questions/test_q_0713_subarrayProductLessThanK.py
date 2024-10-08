import pytest
from q_0713_subarrayProductLessThanK import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([10, 5, 2, 6], 100, 8), ([1, 2, 3], 0, 0)]
)
class TestSolution:
    def test_numSubarrayProductLessThanK(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.numSubarrayProductLessThanK(
                nums,
                k,
            )
            == output
        )
