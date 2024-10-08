import pytest
from q_0068_textJustification import Solution


@pytest.mark.parametrize(
    "words, maxWidth, output",
    [
        (["This", "is", "an", "example", "of", "text", "justification."], 16, None),
        (["What", "must", "be", "acknowledgment", "shall", "be"], 16, None),
        (
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
            None,
        ),
    ],
)
class TestSolution:
    def test_fullJustify(self, words: List[str], maxWidth: int, output: List[str]):
        sc = Solution()
        assert (
            sc.fullJustify(
                words,
                maxWidth,
            )
            == output
        )
