import pytest
from q_2114_maximumNumberOfWordsFoundInSentences import Solution


@pytest.mark.parametrize(
    "sentences, output",
    [
        (
            [
                "alice and bob love leetcode",
                "i think so too",
                "this is great thanks very much",
            ],
            6,
        ),
        (["please wait", "continue to fight", "continue to win"], 3),
    ],
)
class TestSolution:
    def test_mostWordsFound(self, sentences: List[str], output: int):
        sc = Solution()
        assert (
            sc.mostWordsFound(
                sentences,
            )
            == output
        )
