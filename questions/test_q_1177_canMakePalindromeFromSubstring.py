import pytest
from q_1177_canMakePalindromeFromSubstring import Solution


@pytest.mark.parametrize(
    "s, queries, output",
    [
        (
            "abcda",
            [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]],
            [True, False, False, True, True],
        ),
        ("lyb", [[0, 1, 0], [2, 2, 1]], [False, True]),
    ],
)
class TestSolution:
    def test_canMakePaliQueries(
        self, s: str, queries: List[List[int]], output: List[bool]
    ):
        sc = Solution()
        assert (
            sc.canMakePaliQueries(
                s,
                queries,
            )
            == output
        )
