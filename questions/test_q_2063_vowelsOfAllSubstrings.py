import pytest
from q_2063_vowelsOfAllSubstrings import Solution


@pytest.mark.parametrize("word, output", [("aba", 6), ("abc", 3), ("ltcd", 0)])
class TestSolution:
    def test_countVowels(self, word: str, output: int):
        sc = Solution()
        assert (
            sc.countVowels(
                word,
            )
            == output
        )
