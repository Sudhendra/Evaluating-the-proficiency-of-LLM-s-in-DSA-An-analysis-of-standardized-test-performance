import pytest
from q_2942_findWordsContainingCharacter import Solution


@pytest.mark.parametrize(
    "words, x, output",
    [
        (["leet", "code"], "e", [0, 1]),
        (["abc", "bcd", "aaaa", "cbc"], "a", [0, 2]),
        (["abc", "bcd", "aaaa", "cbc"], "z", []),
    ],
)
class TestSolution:
    def test_findWordsContaining(self, words: List[str], x: str, output: List[int]):
        sc = Solution()
        assert (
            sc.findWordsContaining(
                words,
                x,
            )
            == output
        )
