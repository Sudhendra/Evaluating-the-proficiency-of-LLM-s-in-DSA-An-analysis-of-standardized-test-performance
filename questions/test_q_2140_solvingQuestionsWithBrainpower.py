import pytest
from q_2140_solvingQuestionsWithBrainpower import Solution


@pytest.mark.parametrize(
    "questions, output",
    [
        ([[3, 2], [4, 3], [4, 4], [2, 5]], 5),
        ([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 7),
    ],
)
class TestSolution:
    def test_mostPoints(self, questions: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.mostPoints(
                questions,
            )
            == output
        )
