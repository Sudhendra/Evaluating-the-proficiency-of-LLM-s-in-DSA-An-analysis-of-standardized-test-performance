import pytest
from q_1854_maximumPopulationYear import Solution


@pytest.mark.parametrize(
    "logs, output",
    [
        ([[1993, 1999], [2000, 2010]], 1993),
        ([[1950, 1961], [1960, 1971], [1970, 1981]], 1960),
    ],
)
class TestSolution:
    def test_maximumPopulation(self, logs: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maximumPopulation(
                logs,
            )
            == output
        )
