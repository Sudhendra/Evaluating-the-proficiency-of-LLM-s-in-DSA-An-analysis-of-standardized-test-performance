import pytest
from q_1668_maximumRepeatingSubstring import Solution


@pytest.mark.parametrize(
    "sequence, word, output",
    [("ababc", "ab", 2), ("ababc", "ba", 1), ("ababc", "ac", 0)],
)
class TestSolution:
    def test_maxRepeating(self, sequence: str, word: str, output: int):
        sc = Solution()
        assert (
            sc.maxRepeating(
                sequence,
                word,
            )
            == output
        )
