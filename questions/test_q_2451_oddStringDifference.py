import pytest
from q_2451_oddStringDifference import Solution


@pytest.mark.parametrize(
    "words, output",
    [(["adc", "wzy", "abc"], "abc"), (["aaa", "bob", "ccc", "ddd"], "bob")],
)
class TestSolution:
    def test_oddString(self, words: List[str], output: str):
        sc = Solution()
        assert (
            sc.oddString(
                words,
            )
            == output
        )
