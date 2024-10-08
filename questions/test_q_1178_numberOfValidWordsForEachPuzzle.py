import pytest
from q_1178_numberOfValidWordsForEachPuzzle import Solution


@pytest.mark.parametrize(
    "words, puzzles, output",
    [
        (
            ["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
            ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"],
            [1, 1, 3, 2, 4, 0],
        ),
        (
            ["apple", "pleas", "please"],
            ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"],
            [0, 1, 3, 2, 0],
        ),
    ],
)
class TestSolution:
    def test_findNumOfValidWords(
        self, words: List[str], puzzles: List[str], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.findNumOfValidWords(
                words,
                puzzles,
            )
            == output
        )
