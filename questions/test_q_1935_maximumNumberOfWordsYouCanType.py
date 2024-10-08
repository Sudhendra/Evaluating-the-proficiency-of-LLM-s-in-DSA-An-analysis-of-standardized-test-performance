import pytest
from q_1935_maximumNumberOfWordsYouCanType import Solution


@pytest.mark.parametrize(
    "text, brokenLetters, output",
    [("hello world", "ad", 1), ("leet code", "lt", 1), ("leet code", "e", 0)],
)
class TestSolution:
    def test_canBeTypedWords(self, text: str, brokenLetters: str, output: int):
        sc = Solution()
        assert (
            sc.canBeTypedWords(
                text,
                brokenLetters,
            )
            == output
        )
