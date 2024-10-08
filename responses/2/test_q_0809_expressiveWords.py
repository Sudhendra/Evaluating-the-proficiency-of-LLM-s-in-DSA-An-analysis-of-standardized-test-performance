from typing import List
import pytest
from q_0809_expressiveWords import Solution


@pytest.mark.parametrize(
    "s, words, output",
    [
        ("heeellooo", ["hello", "hi", "helo"], 1),
        ("zzzzzyyyyy", ["zzyy", "zy", "zyy"], 3),
    ],
)
class TestSolution:
    def test_expressiveWords(self, s: str, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.expressiveWords(
                s,
                words,
            )
            == output
        )
