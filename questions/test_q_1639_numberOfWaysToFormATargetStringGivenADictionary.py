import pytest
from q_1639_numberOfWaysToFormATargetStringGivenADictionary import Solution


@pytest.mark.parametrize(
    "words, target, output",
    [(["acca", "bbbb", "caca"], "aba", 6), (["abba", "baab"], "bab", 4)],
)
class TestSolution:
    def test_numWays(self, words: List[str], target: str, output: int):
        sc = Solution()
        assert (
            sc.numWays(
                words,
                target,
            )
            == output
        )
