import pytest
from q_1048_longestStringChain import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["a", "b", "ba", "bca", "bda", "bdca"], 4),
        (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
        (["abcd", "dbqca"], 1),
    ],
)
class TestSolution:
    def test_longestStrChain(self, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.longestStrChain(
                words,
            )
            == output
        )
