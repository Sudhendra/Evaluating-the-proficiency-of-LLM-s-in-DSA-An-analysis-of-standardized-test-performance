import pytest
from q_2472_maximumNumberOfNonOverlappingPalindromeSubstrings import Solution


@pytest.mark.parametrize("s, k, output", [("abaccdbbd", 3, 2), ("adbcda", 2, 0)])
class TestSolution:
    def test_maxPalindromes(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.maxPalindromes(
                s,
                k,
            )
            == output
        )
