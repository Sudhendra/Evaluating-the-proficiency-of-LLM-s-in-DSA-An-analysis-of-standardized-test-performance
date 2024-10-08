import pytest
from q_1002_findCommonCharacters import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["bella", "label", "roller"], ["e", "l", "l"]),
        (["cool", "lock", "cook"], ["c", "o"]),
    ],
)
class TestSolution:
    def test_commonChars(self, words: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.commonChars(
                words,
            )
            == output
        )
