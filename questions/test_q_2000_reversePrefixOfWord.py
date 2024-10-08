import pytest
from q_2000_reversePrefixOfWord import Solution


@pytest.mark.parametrize(
    "word, ch, output",
    [("abcdefd", "d", "dcbaefd"), ("xyxzxe", "z", "zxyxxe"), ("abcd", "z", "abcd")],
)
class TestSolution:
    def test_reversePrefix(self, word: str, ch: str, output: str):
        sc = Solution()
        assert (
            sc.reversePrefix(
                word,
                ch,
            )
            == output
        )
