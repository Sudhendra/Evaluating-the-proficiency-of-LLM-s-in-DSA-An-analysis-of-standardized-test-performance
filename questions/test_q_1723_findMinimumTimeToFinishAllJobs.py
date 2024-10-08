import pytest
from q_1723_findMinimumTimeToFinishAllJobs import Solution


@pytest.mark.parametrize(
    "jobs, k, output", [([3, 2, 3], 3, 3), ([1, 2, 4, 7, 8], 2, 11)]
)
class TestSolution:
    def test_minimumTimeRequired(self, jobs: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minimumTimeRequired(
                jobs,
                k,
            )
            == output
        )
