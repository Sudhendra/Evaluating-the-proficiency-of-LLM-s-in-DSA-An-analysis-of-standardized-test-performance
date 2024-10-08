import pytest
from q_0692_topKFrequentWords import Solution


@pytest.mark.parametrize(
    "words, k, output",
    [
        (["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]),
        (
            ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
            4,
            ["the", "is", "sunny", "day"],
        ),
    ],
)
class TestSolution:
    def test_topKFrequent(self, words: List[str], k: int, output: List[str]):
        sc = Solution()
        assert (
            sc.topKFrequent(
                words,
                k,
            )
            == output
        )
