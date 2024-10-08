import pytest
from q_1491_averageSalaryExcludingTheMinimumAndMaximumSalary import Solution


@pytest.mark.parametrize(
    "salary, output", [([4000, 3000, 1000, 2000], 2500.0), ([1000, 2000, 3000], 2000.0)]
)
class TestSolution:
    def test_average(self, salary: List[int], output: float):
        sc = Solution()
        assert (
            sc.average(
                salary,
            )
            == output
        )
