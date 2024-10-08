import pytest
from q_1392_longestHappyPrefix import Solution


@pytest.mark.parametrize("s, output", [("level", "l"), ("ababab", "abab")])
class TestSolution:
    def test_longestPrefix(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.longestPrefix(
                s,
            )
            == output
        )
