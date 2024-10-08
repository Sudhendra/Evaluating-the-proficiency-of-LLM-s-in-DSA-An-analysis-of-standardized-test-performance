import pytest
from q_2024_maximizeTheConfusionOfAnExam import Solution


@pytest.mark.parametrize(
    "answerKey, k, output", [("TTFF", 2, 4), ("TFFT", 1, 3), ("TTFTTFTT", 1, 5)]
)
class TestSolution:
    def test_maxConsecutiveAnswers(self, answerKey: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.maxConsecutiveAnswers(
                answerKey,
                k,
            )
            == output
        )
