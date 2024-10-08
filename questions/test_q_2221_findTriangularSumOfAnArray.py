import pytest
from q_2221_findTriangularSumOfAnArray import Solution


@pytest.mark.parametrize("nums, output", [([1, 2, 3, 4, 5], 8), ([5], 5)])
class TestSolution:
    def test_triangularSum(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.triangularSum(
                nums,
            )
            == output
        )
