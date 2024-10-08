import pytest
from q_2141_maximumRunningTimeOfNComputers import Solution


@pytest.mark.parametrize(
    "n, batteries, output", [(2, [3, 3, 3], 4), (2, [1, 1, 1, 1], 2)]
)
class TestSolution:
    def test_maxRunTime(self, n: int, batteries: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxRunTime(
                n,
                batteries,
            )
            == output
        )
