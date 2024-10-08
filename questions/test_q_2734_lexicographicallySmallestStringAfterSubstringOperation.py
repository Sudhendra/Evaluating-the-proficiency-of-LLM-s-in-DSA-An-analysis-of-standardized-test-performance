import pytest
from q_2734_lexicographicallySmallestStringAfterSubstringOperation import Solution


@pytest.mark.parametrize(
    "s, output", [("cbabc", "baabc"), ("acbbc", "abaab"), ("leetcode", "kddsbncd")]
)
class TestSolution:
    def test_smallestString(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.smallestString(
                s,
            )
            == output
        )
