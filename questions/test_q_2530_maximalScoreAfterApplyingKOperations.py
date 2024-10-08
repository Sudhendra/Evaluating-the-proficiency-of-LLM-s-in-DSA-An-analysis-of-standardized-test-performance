import pytest
from q_2530_maximalScoreAfterApplyingKOperations import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([10, 10, 10, 10, 10], 5, 50), ([1, 10, 3, 3, 3], 3, 17)]
)
class TestSolution:
    def test_maxKelements(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.maxKelements(
                nums,
                k,
            )
            == output
        )
