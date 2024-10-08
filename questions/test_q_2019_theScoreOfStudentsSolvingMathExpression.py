import pytest
from q_2019_theScoreOfStudentsSolvingMathExpression import Solution


@pytest.mark.parametrize(
    "s, answers, output",
    [
        ("7+3*1*2", [20, 13, 42], 7),
        ("3+5*2", [13, 0, 10, 13, 13, 16, 16], 19),
        ("6+0*1", [12, 9, 6, 4, 8, 6], 10),
    ],
)
class TestSolution:
    def test_scoreOfStudents(self, s: str, answers: List[int], output: int):
        sc = Solution()
        assert (
            sc.scoreOfStudents(
                s,
                answers,
            )
            == output
        )
