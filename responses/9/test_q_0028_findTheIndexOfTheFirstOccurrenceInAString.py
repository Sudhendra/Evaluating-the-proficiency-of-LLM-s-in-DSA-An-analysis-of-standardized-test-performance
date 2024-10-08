import pytest
from q_0028_findTheIndexOfTheFirstOccurrenceInAString import Solution


@pytest.mark.parametrize(
    "haystack, needle, output", [("sadbutsad", "sad", 0), ("leetcode", "leeto", -1)]
)
class TestSolution:
    def test_strStr(self, haystack: str, needle: str, output: int):
        sc = Solution()
        assert (
            sc.strStr(
                haystack,
                needle,
            )
            == output
        )
