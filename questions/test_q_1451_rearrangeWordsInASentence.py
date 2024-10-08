import pytest
from q_1451_rearrangeWordsInASentence import Solution


@pytest.mark.parametrize(
    "text, output",
    [
        ("Leetcode is cool", "Is cool leetcode"),
        ("Keep calm and code on", "On and keep calm code"),
        ("To be or not to be", "To be or to be not"),
    ],
)
class TestSolution:
    def test_arrangeWords(self, text: str, output: str):
        sc = Solution()
        assert (
            sc.arrangeWords(
                text,
            )
            == output
        )
