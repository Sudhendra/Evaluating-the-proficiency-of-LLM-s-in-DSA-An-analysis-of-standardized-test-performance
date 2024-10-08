import pytest
from q_2778_sumOfSquaresOfSpecialElements import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 4], 21), ([2, 7, 1, 19, 18, 3], 63)]
)
class TestSolution:
    def test_sumOfSquares(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.sumOfSquares(
                nums,
            )
            == output
        )
