import pytest
from q_1408_stringMatchingInAnArray import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["mass", "as", "hero", "superhero"], ["as", "hero"]),
        (["leetcode", "et", "code"], ["et", "code"]),
        (["blue", "green", "bu"], []),
    ],
)
class TestSolution:
    def test_stringMatching(self, words: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.stringMatching(
                words,
            )
            == output
        )
