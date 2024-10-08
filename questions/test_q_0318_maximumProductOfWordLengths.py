import pytest
from q_0318_maximumProductOfWordLengths import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 16),
        (["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4),
        (["a", "aa", "aaa", "aaaa"], 0),
    ],
)
class TestSolution:
    def test_maxProduct(self, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.maxProduct(
                words,
            )
            == output
        )
