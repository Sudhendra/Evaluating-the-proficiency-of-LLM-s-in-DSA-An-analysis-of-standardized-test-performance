import pytest
from q_0395_longestSubstringWithAtLeastKRepeatingCharacters import Solution


@pytest.mark.parametrize("s, k, output", [("aaabb", 3, 3), ("ababbc", 2, 5)])
class TestSolution:
    def test_longestSubstring(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.longestSubstring(
                s,
                k,
            )
            == output
        )
