import pytest
from q_1957_deleteCharactersToMakeFancyString import Solution


@pytest.mark.parametrize(
    "s, output", [("leeetcode", "leetcode"), ("aaabaaaa", "aabaa"), ("aab", "aab")]
)
class TestSolution:
    def test_makeFancyString(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.makeFancyString(
                s,
            )
            == output
        )
