import pytest
from q_2386_findTheKSumOfAnArray import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([2, 4, -2], 5, 2), ([1, -2, 3, 4, -10, 12], 16, 10)]
)
class TestSolution:
    def test_kSum(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.kSum(
                nums,
                k,
            )
            == output
        )
