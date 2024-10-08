import pytest
from q_2594_minimumTimeToRepairCars import Solution


@pytest.mark.parametrize(
    "ranks, cars, output", [([4, 2, 3, 1], 10, 16), ([5, 1, 8], 6, 16)]
)
class TestSolution:
    def test_repairCars(self, ranks: List[int], cars: int, output: int):
        sc = Solution()
        assert (
            sc.repairCars(
                ranks,
                cars,
            )
            == output
        )
