import pytest
from q_2030_smallestKLengthSubsequenceWithOccurrencesOfALetter import Solution


@pytest.mark.parametrize(
    "s, k, letter, repetition, output",
    [
        ("leet", 3, "e", 1, "eet"),
        ("leetcode", 4, "e", 2, "ecde"),
        ("bb", 2, "b", 2, "bb"),
    ],
)
class TestSolution:
    def test_smallestSubsequence(
        self, s: str, k: int, letter: str, repetition: int, output: str
    ):
        sc = Solution()
        assert (
            sc.smallestSubsequence(
                s,
                k,
                letter,
                repetition,
            )
            == output
        )
