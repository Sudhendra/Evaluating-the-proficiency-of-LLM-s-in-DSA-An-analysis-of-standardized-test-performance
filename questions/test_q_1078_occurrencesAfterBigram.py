import pytest
from q_1078_occurrencesAfterBigram import Solution


@pytest.mark.parametrize(
    "text, first, second, output",
    [
        (
            "alice is a good girl she is a good student",
            "a",
            "good",
            ["girl", "student"],
        ),
        ("we will we will rock you", "we", "will", ["we", "rock"]),
    ],
)
class TestSolution:
    def test_findOcurrences(
        self, text: str, first: str, second: str, output: List[str]
    ):
        sc = Solution()
        assert (
            sc.findOcurrences(
                text,
                first,
                second,
            )
            == output
        )
