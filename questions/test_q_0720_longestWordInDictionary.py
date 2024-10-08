import pytest
from q_0720_longestWordInDictionary import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["w", "wo", "wor", "worl", "world"], "world"),
        (["a", "banana", "app", "appl", "ap", "apply", "apple"], "apple"),
    ],
)
class TestSolution:
    def test_longestWord(self, words: List[str], output: str):
        sc = Solution()
        assert (
            sc.longestWord(
                words,
            )
            == output
        )
