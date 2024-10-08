import pytest
from q_1424_diagonalTraverseIi import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 4, 2, 7, 5, 3, 8, 6, 9]),
        (
            [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]],
            [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16],
        ),
    ],
)
class TestSolution:
    def test_findDiagonalOrder(self, nums: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.findDiagonalOrder(
                nums,
            )
            == output
        )
