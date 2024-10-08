import pytest
from q_1910_removeAllOccurrencesOfASubstring import Solution


@pytest.mark.parametrize(
    "s, part, output", [("daabcbaabcbc", "abc", "dab"), ("axxxxyyyyb", "xy", "ab")]
)
class TestSolution:
    def test_removeOccurrences(self, s: str, part: str, output: str):
        sc = Solution()
        assert (
            sc.removeOccurrences(
                s,
                part,
            )
            == output
        )
