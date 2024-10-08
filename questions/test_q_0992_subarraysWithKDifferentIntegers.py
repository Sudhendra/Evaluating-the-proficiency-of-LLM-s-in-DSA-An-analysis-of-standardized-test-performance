import pytest
from q_0992_subarraysWithKDifferentIntegers import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 2, 1, 2, 3], 2, 7), ([1, 2, 1, 3, 4], 3, 3)]
)
class TestSolution:
    def test_subarraysWithKDistinct(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.subarraysWithKDistinct(
                nums,
                k,
            )
            == output
        )
