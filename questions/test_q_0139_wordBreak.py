import pytest
from q_0139_wordBreak import Solution


@pytest.mark.parametrize(
    "s, wordDict, output",
    [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ],
)
class TestSolution:
    def test_wordBreak(self, s: str, wordDict: List[str], output: bool):
        sc = Solution()
        assert (
            sc.wordBreak(
                s,
                wordDict,
            )
            == output
        )
