import pytest
from q_0884_uncommonWordsFromTwoSentences import Solution


@pytest.mark.parametrize(
    "s1, s2, output",
    [
        ("this apple is sweet", "this apple is sour", ["sweet", "sour"]),
        ("apple apple", "banana", ["banana"]),
    ],
)
class TestSolution:
    def test_uncommonFromSentences(self, s1: str, s2: str, output: List[str]):
        sc = Solution()
        assert (
            sc.uncommonFromSentences(
                s1,
                s2,
            )
            == output
        )
