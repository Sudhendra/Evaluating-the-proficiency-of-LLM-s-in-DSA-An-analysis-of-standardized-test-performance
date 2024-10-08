import pytest
from q_0943_findTheShortestSuperstring import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["alex", "loves", "leetcode"], "alexlovesleetcode"),
        (["catg", "ctaagt", "gcta", "ttca", "atgcatc"], "gctaagttcatgcatc"),
    ],
)
class TestSolution:
    def test_shortestSuperstring(self, words: List[str], output: str):
        sc = Solution()
        assert (
            sc.shortestSuperstring(
                words,
            )
            == output
        )
