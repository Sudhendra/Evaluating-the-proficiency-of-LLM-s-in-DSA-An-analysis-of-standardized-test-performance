import pytest
from q_2798_numberOfEmployeesWhoMetTheTarget import Solution


@pytest.mark.parametrize(
    "hours, target, output", [([0, 1, 2, 3, 4], 2, 3), ([5, 1, 4, 2, 2], 6, 0)]
)
class TestSolution:
    def test_numberOfEmployeesWhoMetTarget(
        self, hours: List[int], target: int, output: int
    ):
        sc = Solution()
        assert (
            sc.numberOfEmployeesWhoMetTarget(
                hours,
                target,
            )
            == output
        )
