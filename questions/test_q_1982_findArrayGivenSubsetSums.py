import pytest
from q_1982_findArrayGivenSubsetSums import Solution


@pytest.mark.parametrize(
    "n, sums, output",
    [
        (3, [-3, -2, -1, 0, 0, 1, 2, 3], [1, 2, -3]),
        (2, [0, 0, 0, 0], [0, 0]),
        (4, [0, 0, 5, 5, 4, -1, 4, 9, 9, -1, 4, 3, 4, 8, 3, 8], [0, -1, 4, 5]),
    ],
)
class TestSolution:
    def test_recoverArray(self, n: int, sums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.recoverArray(
                n,
                sums,
            )
            == output
        )
