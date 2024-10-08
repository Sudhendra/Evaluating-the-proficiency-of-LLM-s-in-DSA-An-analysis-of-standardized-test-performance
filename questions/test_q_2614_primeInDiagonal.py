import pytest
from q_2614_primeInDiagonal import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([[1, 2, 3], [5, 6, 7], [9, 10, 11]], 11),
        ([[1, 2, 3], [5, 17, 7], [9, 11, 10]], 17),
    ],
)
class TestSolution:
    def test_diagonalPrime(self, nums: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.diagonalPrime(
                nums,
            )
            == output
        )
