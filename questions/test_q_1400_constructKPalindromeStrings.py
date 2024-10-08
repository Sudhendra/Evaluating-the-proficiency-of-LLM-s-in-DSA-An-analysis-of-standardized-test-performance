import pytest
from q_1400_constructKPalindromeStrings import Solution


@pytest.mark.parametrize(
    "s, k, output", [("annabelle", 2, True), ("leetcode", 3, False), ("true", 4, True)]
)
class TestSolution:
    def test_canConstruct(self, s: str, k: int, output: bool):
        sc = Solution()
        assert (
            sc.canConstruct(
                s,
                k,
            )
            == output
        )
