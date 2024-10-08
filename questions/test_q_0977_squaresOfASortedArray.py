import pytest
from q_0977_squaresOfASortedArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ],
)
class TestSolution:
    def test_sortedSquares(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.sortedSquares(
                nums,
            )
            == output
        )
