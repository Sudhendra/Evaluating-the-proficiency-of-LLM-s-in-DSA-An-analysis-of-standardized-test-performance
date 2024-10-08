import pytest
from q_2207_maximizeNumberOfSubsequencesInAString import Solution


@pytest.mark.parametrize(
    "text, pattern, output", [("abdcdbc", "ac", 4), ("aabb", "ab", 6)]
)
class TestSolution:
    def test_maximumSubsequenceCount(self, text: str, pattern: str, output: int):
        sc = Solution()
        assert (
            sc.maximumSubsequenceCount(
                text,
                pattern,
            )
            == output
        )
