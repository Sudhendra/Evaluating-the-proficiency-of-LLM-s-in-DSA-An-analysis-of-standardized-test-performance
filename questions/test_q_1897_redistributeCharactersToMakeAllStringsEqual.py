import pytest
from q_1897_redistributeCharactersToMakeAllStringsEqual import Solution


@pytest.mark.parametrize(
    "words, output", [(["abc", "aabc", "bc"], True), (["ab", "a"], False)]
)
class TestSolution:
    def test_makeEqual(self, words: List[str], output: bool):
        sc = Solution()
        assert (
            sc.makeEqual(
                words,
            )
            == output
        )
