import pytest
from q_2800_shortestStringThatContainsThreeStrings import Solution


@pytest.mark.parametrize(
    "a, b, c, output", [("abc", "bca", "aaa", "aaabca"), ("ab", "ba", "aba", "aba")]
)
class TestSolution:
    def test_minimumString(self, a: str, b: str, c: str, output: str):
        sc = Solution()
        assert (
            sc.minimumString(
                a,
                b,
                c,
            )
            == output
        )
