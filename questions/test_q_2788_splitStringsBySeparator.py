import pytest
from q_2788_splitStringsBySeparator import Solution


@pytest.mark.parametrize(
    "words, separator, output",
    [
        (
            ["one.two.three", "four.five", "six"],
            ".",
            ["one", "two", "three", "four", "five", "six"],
        ),
        (["$easy$", "$problem$"], "$", ["easy", "problem"]),
        (["|||"], "|", []),
    ],
)
class TestSolution:
    def test_splitWordsBySeparator(
        self, words: List[str], separator: str, output: List[str]
    ):
        sc = Solution()
        assert (
            sc.splitWordsBySeparator(
                words,
                separator,
            )
            == output
        )
