import pytest
from q_1347_minimumNumberOfStepsToMakeTwoStringsAnagram import Solution


@pytest.mark.parametrize(
    "s, t, output",
    [("bab", "aba", 1), ("leetcode", "practice", 5), ("anagram", "mangaar", 0)],
)
class TestSolution:
    def test_minSteps(self, s: str, t: str, output: int):
        sc = Solution()
        assert (
            sc.minSteps(
                s,
                t,
            )
            == output
        )
