import pytest
from q_2609_findTheLongestBalancedSubstringOfABinaryString import Solution


@pytest.mark.parametrize("s, output", [("01000111", 6), ("00111", 4), ("111", 0)])
class TestSolution:
    def test_findTheLongestBalancedSubstring(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.findTheLongestBalancedSubstring(
                s,
            )
            == output
        )
