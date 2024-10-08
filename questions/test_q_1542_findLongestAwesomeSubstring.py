import pytest
from q_1542_findLongestAwesomeSubstring import Solution


@pytest.mark.parametrize("s, output", [("3242415", 5), ("12345678", 1), ("213123", 6)])
class TestSolution:
    def test_longestAwesome(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.longestAwesome(
                s,
            )
            == output
        )
