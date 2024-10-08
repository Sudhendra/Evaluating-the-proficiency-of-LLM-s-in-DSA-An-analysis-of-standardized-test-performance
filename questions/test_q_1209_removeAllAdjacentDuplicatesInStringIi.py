import pytest
from q_1209_removeAllAdjacentDuplicatesInStringIi import Solution


@pytest.mark.parametrize(
    "s, k, output",
    [
        ("abcd", 2, "abcd"),
        ("deeedbbcccbdaa", 3, "aa"),
        ("pbbcggttciiippooaais", 2, "ps"),
    ],
)
class TestSolution:
    def test_removeDuplicates(self, s: str, k: int, output: str):
        sc = Solution()
        assert (
            sc.removeDuplicates(
                s,
                k,
            )
            == output
        )
