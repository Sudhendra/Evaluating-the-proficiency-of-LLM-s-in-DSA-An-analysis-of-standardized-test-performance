import pytest
from q_0792_numberOfMatchingSubsequences import Solution


@pytest.mark.parametrize(
    "s, words, output",
    [
        ("abcde", ["a", "bb", "acd", "ace"], 3),
        ("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"], 2),
    ],
)
class TestSolution:
    def test_numMatchingSubseq(self, s: str, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.numMatchingSubseq(
                s,
                words,
            )
            == output
        )
