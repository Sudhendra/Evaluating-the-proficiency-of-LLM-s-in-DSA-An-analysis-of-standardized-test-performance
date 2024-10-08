import pytest
from q_2953_countCompleteSubstrings import Solution


@pytest.mark.parametrize("word, k, output", [("igigee", 2, 3), ("aaabbbccc", 3, 6)])
class TestSolution:
    def test_countCompleteSubstrings(self, word: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.countCompleteSubstrings(
                word,
                k,
            )
            == output
        )
