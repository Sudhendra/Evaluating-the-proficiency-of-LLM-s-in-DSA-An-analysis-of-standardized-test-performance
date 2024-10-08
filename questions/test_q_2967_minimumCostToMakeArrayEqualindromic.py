import pytest
from q_2967_minimumCostToMakeArrayEqualindromic import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 3, 4, 5], 6), ([10, 12, 13, 14, 15], 11), ([22, 33, 22, 33, 22], 22)],
)
class TestSolution:
    def test_minimumCost(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumCost(
                nums,
            )
            == output
        )
