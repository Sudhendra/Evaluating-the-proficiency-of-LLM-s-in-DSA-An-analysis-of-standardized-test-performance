import pytest
from q_1915_numberOfWonderfulSubstrings import Solution


@pytest.mark.parametrize("word, output", [("aba", 4), ("aabb", 9), ("he", 2)])
class TestSolution:
    def test_wonderfulSubstrings(self, word: str, output: int):
        sc = Solution()
        assert (
            sc.wonderfulSubstrings(
                word,
            )
            == output
        )
