import pytest
from q_2014_longestSubsequenceRepeatedKTimes import Solution


@pytest.mark.parametrize(
    "s, k, output", [("letsleetcode", 2, "let"), ("bb", 2, "b"), ("ab", 2, "")]
)
class TestSolution:
    def test_longestSubsequenceRepeatedK(self, s: str, k: int, output: str):
        sc = Solution()
        assert (
            sc.longestSubsequenceRepeatedK(
                s,
                k,
            )
            == output
        )
