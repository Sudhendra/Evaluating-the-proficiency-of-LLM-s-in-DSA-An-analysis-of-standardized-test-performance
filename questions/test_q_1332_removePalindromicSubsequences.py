import pytest
from q_1332_removePalindromicSubsequences import Solution


@pytest.mark.parametrize("s, output", [("ababa", 1), ("abb", 2), ("baabb", 2)])
class TestSolution:
    def test_removePalindromeSub(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.removePalindromeSub(
                s,
            )
            == output
        )
