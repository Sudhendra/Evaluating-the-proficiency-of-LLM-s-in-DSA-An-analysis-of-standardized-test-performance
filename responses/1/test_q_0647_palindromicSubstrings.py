import pytest
from q_0647_palindromicSubstrings import Solution


@pytest.mark.parametrize("s, output", [("abc", 3), ("aaa", 6)])
class TestSolution:
    def test_countSubstrings(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.countSubstrings(
                s,
            )
            == output
        )
