import pytest
from q_2781_lengthOfTheLongestValidSubstring import Solution


@pytest.mark.parametrize(
    "word, forbidden, output",
    [("cbaaaabc", ["aaa", "cb"], 4), ("leetcode", ["de", "le", "e"], 4)],
)
class TestSolution:
    def test_longestValidSubstring(self, word: str, forbidden: List[str], output: int):
        sc = Solution()
        assert (
            sc.longestValidSubstring(
                word,
                forbidden,
            )
            == output
        )
