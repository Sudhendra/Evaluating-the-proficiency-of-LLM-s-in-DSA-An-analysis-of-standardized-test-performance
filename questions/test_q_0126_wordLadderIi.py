import pytest
from q_0126_wordLadderIi import Solution


@pytest.mark.parametrize(
    "beginWord, endWord, wordList, output",
    [
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"],
            [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]],
        ),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], []),
    ],
)
class TestSolution:
    def test_findLadders(
        self, beginWord: str, endWord: str, wordList: List[str], output: List[List[str]]
    ):
        sc = Solution()
        assert (
            sc.findLadders(
                beginWord,
                endWord,
                wordList,
            )
            == output
        )
