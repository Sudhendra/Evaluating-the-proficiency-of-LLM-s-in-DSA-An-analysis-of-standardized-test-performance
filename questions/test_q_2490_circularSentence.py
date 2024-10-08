import pytest
from q_2490_circularSentence import Solution


@pytest.mark.parametrize(
    "sentence, output",
    [
        ("leetcode exercises sound delightful", True),
        ("eetcode", True),
        ("Leetcode is cool", False),
    ],
)
class TestSolution:
    def test_isCircularSentence(self, sentence: str, output: bool):
        sc = Solution()
        assert (
            sc.isCircularSentence(
                sentence,
            )
            == output
        )
