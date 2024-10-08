import pytest
from q_0212_wordSearchIi import Solution


@pytest.mark.parametrize(
    "board, words, output",
    [
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            ["eat", "oath"],
        ),
        ([["a", "b"], ["c", "d"]], ["abcb"], []),
    ],
)
class TestSolution:
    def test_findWords(
        self, board: List[List[str]], words: List[str], output: List[str]
    ):
        sc = Solution()
        assert (
            sc.findWords(
                board,
                words,
            )
            == output
        )
