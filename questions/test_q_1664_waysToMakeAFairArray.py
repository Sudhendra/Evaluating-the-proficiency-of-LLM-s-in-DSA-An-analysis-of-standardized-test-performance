import pytest
from q_1664_waysToMakeAFairArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 1, 6, 4], 1), ([1, 1, 1], 3), ([1, 2, 3], 0)]
)
class TestSolution:
    def test_waysToMakeFair(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.waysToMakeFair(
                nums,
            )
            == output
        )
