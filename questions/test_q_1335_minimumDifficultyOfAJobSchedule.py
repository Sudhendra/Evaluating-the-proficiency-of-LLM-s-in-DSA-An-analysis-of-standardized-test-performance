import pytest
from q_1335_minimumDifficultyOfAJobSchedule import Solution


@pytest.mark.parametrize(
    "jobDifficulty, d, output",
    [([6, 5, 4, 3, 2, 1], 2, 7), ([9, 9, 9], 4, -1), ([1, 1, 1], 3, 3)],
)
class TestSolution:
    def test_minDifficulty(self, jobDifficulty: List[int], d: int, output: int):
        sc = Solution()
        assert (
            sc.minDifficulty(
                jobDifficulty,
                d,
            )
            == output
        )
