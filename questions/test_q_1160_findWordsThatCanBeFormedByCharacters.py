import pytest
from q_1160_findWordsThatCanBeFormedByCharacters import Solution


@pytest.mark.parametrize(
    "words, chars, output",
    [
        (["cat", "bt", "hat", "tree"], "atach", 6),
        (["hello", "world", "leetcode"], "welldonehoneyr", 10),
    ],
)
class TestSolution:
    def test_countCharacters(self, words: List[str], chars: str, output: int):
        sc = Solution()
        assert (
            sc.countCharacters(
                words,
                chars,
            )
            == output
        )
