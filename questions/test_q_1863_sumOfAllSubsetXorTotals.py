import pytest
from q_1863_sumOfAllSubsetXorTotals import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 3], 6), ([5, 1, 6], 28), ([3, 4, 5, 6, 7, 8], 480)]
)
class TestSolution:
    def test_subsetXORSum(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.subsetXORSum(
                nums,
            )
            == output
        )
