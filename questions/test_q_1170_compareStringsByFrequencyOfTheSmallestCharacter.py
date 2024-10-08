import pytest
from q_1170_compareStringsByFrequencyOfTheSmallestCharacter import Solution


@pytest.mark.parametrize(
    "queries, words, output",
    [(["cbd"], ["zaaaz"], [1]), (["bbb", "cc"], ["a", "aa", "aaa", "aaaa"], [1, 2])],
)
class TestSolution:
    def test_numSmallerByFrequency(
        self, queries: List[str], words: List[str], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.numSmallerByFrequency(
                queries,
                words,
            )
            == output
        )
