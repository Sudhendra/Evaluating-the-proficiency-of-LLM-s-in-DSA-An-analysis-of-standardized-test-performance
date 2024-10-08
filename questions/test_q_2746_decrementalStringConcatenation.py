import pytest
from q_2746_decrementalStringConcatenation import Solution


@pytest.mark.parametrize(
    "words, output",
    [(["aa", "ab", "bc"], 4), (["ab", "b"], 2), (["aaa", "c", "aba"], 6)],
)
class TestSolution:
    def test_minimizeConcatenatedLength(self, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.minimizeConcatenatedLength(
                words,
            )
            == output
        )
