import pytest
from q_0967_numbersWithSameConsecutiveDifferences import Solution


@pytest.mark.parametrize(
    "n, k, output",
    [
        (3, 7, [181, 292, 707, 818, 929]),
        (2, 1, [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]),
    ],
)
class TestSolution:
    def test_numsSameConsecDiff(self, n: int, k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.numsSameConsecDiff(
                n,
                k,
            )
            == output
        )
