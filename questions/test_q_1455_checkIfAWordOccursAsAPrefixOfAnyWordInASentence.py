import pytest
from q_1455_checkIfAWordOccursAsAPrefixOfAnyWordInASentence import Solution


@pytest.mark.parametrize(
    "sentence, searchWord, output",
    [
        ("i love eating burger", "burg", 4),
        ("this problem is an easy problem", "pro", 2),
        ("i am tired", "you", -1),
    ],
)
class TestSolution:
    def test_isPrefixOfWord(self, sentence: str, searchWord: str, output: int):
        sc = Solution()
        assert (
            sc.isPrefixOfWord(
                sentence,
                searchWord,
            )
            == output
        )
