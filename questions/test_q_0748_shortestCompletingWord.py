import pytest
from q_0748_shortestCompletingWord import Solution


@pytest.mark.parametrize(
    "licensePlate, words, output",
    [
        ("1s3 PSt", ["step", "steps", "stripe", "stepple"], "steps"),
        ("1s3 456", ["looks", "pest", "stew", "show"], "pest"),
    ],
)
class TestSolution:
    def test_shortestCompletingWord(
        self, licensePlate: str, words: List[str], output: str
    ):
        sc = Solution()
        assert (
            sc.shortestCompletingWord(
                licensePlate,
                words,
            )
            == output
        )
