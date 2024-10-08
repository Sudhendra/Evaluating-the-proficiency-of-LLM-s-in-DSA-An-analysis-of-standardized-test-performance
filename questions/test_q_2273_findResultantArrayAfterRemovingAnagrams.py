import pytest
from q_2273_findResultantArrayAfterRemovingAnagrams import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["abba", "baba", "bbaa", "cd", "cd"], ["abba", "cd"]),
        (["a", "b", "c", "d", "e"], ["a", "b", "c", "d", "e"]),
    ],
)
class TestSolution:
    def test_removeAnagrams(self, words: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.removeAnagrams(
                words,
            )
            == output
        )
