import pytest
from q_2904_shortestAndLexicographicallySmallestBeautifulString import Solution


@pytest.mark.parametrize(
    "s, k, output", [("100011001", 3, "11001"), ("1011", 2, "11"), ("000", 1, "")]
)
class TestSolution:
    def test_shortestBeautifulSubstring(self, s: str, k: int, output: str):
        sc = Solution()
        assert (
            sc.shortestBeautifulSubstring(
                s,
                k,
            )
            == output
        )
