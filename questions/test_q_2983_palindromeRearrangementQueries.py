import pytest
from q_2983_palindromeRearrangementQueries import Solution


@pytest.mark.parametrize(
    "s, queries, output",
    [
        ("abcabc", [[1, 1, 3, 5], [0, 2, 5, 5]], [True, True]),
        ("abbcdecbba", [[0, 2, 7, 9]], [False]),
        ("acbcab", [[1, 2, 4, 5]], [True]),
    ],
)
class TestSolution:
    def test_canMakePalindromeQueries(
        self, s: str, queries: List[List[int]], output: List[bool]
    ):
        sc = Solution()
        assert (
            sc.canMakePalindromeQueries(
                s,
                queries,
            )
            == output
        )
