import pytest
from q_1880_checkIfWordEqualsSummationOfTwoWords import Solution


@pytest.mark.parametrize(
    "firstWord, secondWord, targetWord, output",
    [
        ("acb", "cba", "cdb", True),
        ("aaa", "a", "aab", False),
        ("aaa", "a", "aaaa", True),
    ],
)
class TestSolution:
    def test_isSumEqual(
        self, firstWord: str, secondWord: str, targetWord: str, output: bool
    ):
        sc = Solution()
        assert (
            sc.isSumEqual(
                firstWord,
                secondWord,
                targetWord,
            )
            == output
        )
