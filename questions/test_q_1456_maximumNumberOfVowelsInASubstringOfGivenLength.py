import pytest
from q_1456_maximumNumberOfVowelsInASubstringOfGivenLength import Solution


@pytest.mark.parametrize(
    "s, k, output", [("abciiidef", 3, 3), ("aeiou", 2, 2), ("leetcode", 3, 2)]
)
class TestSolution:
    def test_maxVowels(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.maxVowels(
                s,
                k,
            )
            == output
        )
