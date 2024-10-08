import pytest
from q_0044_wildcardMatching import Solution


@pytest.mark.parametrize(
    "s, p, output", [("aa", "a", False), ("aa", "*", True), ("cb", "?a", False)]
)
class TestSolution:
    def test_isMatch(self, s: str, p: str, output: bool):
        sc = Solution()
        assert (
            sc.isMatch(
                s,
                p,
            )
            == output
        )
