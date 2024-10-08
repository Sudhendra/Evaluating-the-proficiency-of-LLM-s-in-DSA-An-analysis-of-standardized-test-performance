import pytest
from q_3044_mostFrequentPrime import Solution


@pytest.mark.parametrize(
    "mat, output",
    [
        ([[1, 1], [9, 9], [1, 1]], 19),
        ([[7]], -1),
        ([[9, 7, 8], [4, 6, 5], [2, 8, 6]], 97),
    ],
)
class TestSolution:
    def test_mostFrequentPrime(self, mat: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.mostFrequentPrime(
                mat,
            )
            == output
        )
