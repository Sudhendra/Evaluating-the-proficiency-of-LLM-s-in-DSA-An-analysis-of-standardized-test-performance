import pytest
from q_2586_countTheNumberOfVowelStringsInRange import Solution


@pytest.mark.parametrize(
    "words, left, right, output",
    [(["are", "amy", "u"], 0, 2, 2), (["hey", "aeo", "mu", "ooo", "artro"], 1, 4, 3)],
)
class TestSolution:
    def test_vowelStrings(self, words: List[str], left: int, right: int, output: int):
        sc = Solution()
        assert (
            sc.vowelStrings(
                words,
                left,
                right,
            )
            == output
        )
