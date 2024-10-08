import pytest
from q_2512_rewardTopKStudents import Solution


@pytest.mark.parametrize(
    "positive_feedback, negative_feedback, report, student_id, k, output",
    [
        (
            ["smart", "brilliant", "studious"],
            ["not"],
            ["this student is studious", "the student is smart"],
            [1, 2],
            2,
            [1, 2],
        ),
        (
            ["smart", "brilliant", "studious"],
            ["not"],
            ["this student is not studious", "the student is smart"],
            [1, 2],
            2,
            [2, 1],
        ),
    ],
)
class TestSolution:
    def test_topStudents(
        self,
        positive_feedback: List[str],
        negative_feedback: List[str],
        report: List[str],
        student_id: List[int],
        k: int,
        output: List[int],
    ):
        sc = Solution()
        assert (
            sc.topStudents(
                positive_feedback,
                negative_feedback,
                report,
                student_id,
                k,
            )
            == output
        )
