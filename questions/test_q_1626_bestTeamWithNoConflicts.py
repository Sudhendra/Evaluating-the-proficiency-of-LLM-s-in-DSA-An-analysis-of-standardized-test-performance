import pytest
from q_1626_bestTeamWithNoConflicts import Solution


@pytest.mark.parametrize(
    "scores, ages, output",
    [
        ([1, 3, 5, 10, 15], [1, 2, 3, 4, 5], 34),
        ([4, 5, 6, 5], [2, 1, 2, 1], 16),
        ([1, 2, 3, 5], [8, 9, 10, 1], 6),
    ],
)
class TestSolution:
    def test_bestTeamScore(self, scores: List[int], ages: List[int], output: int):
        sc = Solution()
        assert (
            sc.bestTeamScore(
                scores,
                ages,
            )
            == output
        )
