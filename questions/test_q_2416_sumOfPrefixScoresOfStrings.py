import pytest
from q_2416_sumOfPrefixScoresOfStrings import Solution


@pytest.mark.parametrize(
    "words, output", [(["abc", "ab", "bc", "b"], [5, 4, 3, 2]), (["abcd"], [4])]
)
class TestSolution:
    def test_sumPrefixScores(self, words: List[str], output: List[int]):
        sc = Solution()
        assert (
            sc.sumPrefixScores(
                words,
            )
            == output
        )
