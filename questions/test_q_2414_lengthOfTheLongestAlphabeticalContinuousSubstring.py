import pytest
from q_2414_lengthOfTheLongestAlphabeticalContinuousSubstring import Solution


@pytest.mark.parametrize("s, output", [("abacaba", 2), ("abcde", 5)])
class TestSolution:
    def test_longestContinuousSubstring(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.longestContinuousSubstring(
                s,
            )
            == output
        )
