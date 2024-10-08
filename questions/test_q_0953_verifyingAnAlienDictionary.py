import pytest
from q_0953_verifyingAnAlienDictionary import Solution


@pytest.mark.parametrize(
    "words, order, output",
    [
        (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
        (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False),
        (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False),
    ],
)
class TestSolution:
    def test_isAlienSorted(self, words: List[str], order: str, output: bool):
        sc = Solution()
        assert (
            sc.isAlienSorted(
                words,
                order,
            )
            == output
        )
