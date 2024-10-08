import pytest
from q_2062_countVowelSubstringsOfAString import Solution


@pytest.mark.parametrize(
    "word, output", [("aeiouu", 2), ("unicornarihan", 0), ("cuaieuouac", 7)]
)
class TestSolution:
    def test_countVowelSubstrings(self, word: str, output: int):
        sc = Solution()
        assert (
            sc.countVowelSubstrings(
                word,
            )
            == output
        )
