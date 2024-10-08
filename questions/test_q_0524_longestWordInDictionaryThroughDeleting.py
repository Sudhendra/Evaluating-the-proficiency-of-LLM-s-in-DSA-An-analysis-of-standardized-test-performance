import pytest
from q_0524_longestWordInDictionaryThroughDeleting import Solution


@pytest.mark.parametrize(
    "s, dictionary, output",
    [
        ("abpcplea", ["ale", "apple", "monkey", "plea"], "apple"),
        ("abpcplea", ["a", "b", "c"], "a"),
    ],
)
class TestSolution:
    def test_findLongestWord(self, s: str, dictionary: List[str], output: str):
        sc = Solution()
        assert (
            sc.findLongestWord(
                s,
                dictionary,
            )
            == output
        )
