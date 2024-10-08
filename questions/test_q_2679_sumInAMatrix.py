import pytest
from q_2679_sumInAMatrix import Solution


@pytest.mark.parametrize(
    "nums, output", [([[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]], 15), ([[1]], 1)]
)
class TestSolution:
    def test_matrixSum(self, nums: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.matrixSum(
                nums,
            )
            == output
        )
