import pytest
from q_1859_sortingTheSentence import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("is2 sentence4 This1 a3", "This is a sentence"),
        ("Myself2 Me1 I4 and3", "Me Myself and I"),
    ],
)
class TestSolution:
    def test_sortSentence(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.sortSentence(
                s,
            )
            == output
        )
