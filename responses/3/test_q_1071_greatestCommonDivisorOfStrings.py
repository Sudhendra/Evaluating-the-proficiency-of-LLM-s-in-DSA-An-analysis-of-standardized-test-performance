import pytest
from q_1071_greatestCommonDivisorOfStrings import Solution


@pytest.mark.parametrize(
    "str1, str2, output",
    [("ABCABC", "ABC", "ABC"), ("ABABAB", "ABAB", "AB"), ("LEET", "CODE", "")],
)
class TestSolution:
    def test_gcdOfStrings(self, str1: str, str2: str, output: str):
        sc = Solution()
        assert (
            sc.gcdOfStrings(
                str1,
                str2,
            )
            == output
        )
