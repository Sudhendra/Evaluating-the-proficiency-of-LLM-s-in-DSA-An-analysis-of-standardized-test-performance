import pytest
from q_0648_replaceWords import Solution


@pytest.mark.parametrize(
    "dictionary, sentence, output",
    [
        (
            ["cat", "bat", "rat"],
            "the cattle was rattled by the battery",
            "the cat was rat by the bat",
        ),
        (["a", "b", "c"], "aadsfasf absbs bbab cadsfafs", "a a b c"),
    ],
)
class TestSolution:
    def test_replaceWords(self, dictionary: List[str], sentence: str, output: str):
        sc = Solution()
        assert (
            sc.replaceWords(
                dictionary,
                sentence,
            )
            == output
        )
