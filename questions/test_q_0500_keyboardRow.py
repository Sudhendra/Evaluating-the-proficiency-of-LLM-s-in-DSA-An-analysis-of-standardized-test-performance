import pytest
from q_0500_keyboardRow import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"]),
        (["omk"], []),
        (["adsdf", "sfd"], ["adsdf", "sfd"]),
    ],
)
class TestSolution:
    def test_findWords(self, words: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.findWords(
                words,
            )
            == output
        )
