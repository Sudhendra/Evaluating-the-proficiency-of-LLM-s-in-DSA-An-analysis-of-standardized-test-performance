import pytest
from q_0893_groupsOfSpecialEquivalentStrings import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"], 3),
        (["abc", "acb", "bac", "bca", "cab", "cba"], 3),
    ],
)
class TestSolution:
    def test_numSpecialEquivGroups(self, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.numSpecialEquivGroups(
                words,
            )
            == output
        )
