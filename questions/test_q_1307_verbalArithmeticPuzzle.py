import pytest
from q_1307_verbalArithmeticPuzzle import Solution


@pytest.mark.parametrize(
    "words, result, output",
    [
        (["SEND", "MORE"], "MONEY", True),
        (["SIX", "SEVEN", "SEVEN"], "TWENTY", True),
        (["LEET", "CODE"], "POINT", False),
    ],
)
class TestSolution:
    def test_isSolvable(self, words: List[str], result: str, output: bool):
        sc = Solution()
        assert (
            sc.isSolvable(
                words,
                result,
            )
            == output
        )
