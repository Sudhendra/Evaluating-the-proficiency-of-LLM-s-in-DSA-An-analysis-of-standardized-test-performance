import pytest
from q_2105_wateringPlantsIi import Solution


@pytest.mark.parametrize(
    "plants, capacityA, capacityB, output",
    [([2, 2, 3, 3], 5, 5, 1), ([2, 2, 3, 3], 3, 4, 2), ([5], 10, 8, 0)],
)
class TestSolution:
    def test_minimumRefill(
        self, plants: List[int], capacityA: int, capacityB: int, output: int
    ):
        sc = Solution()
        assert (
            sc.minimumRefill(
                plants,
                capacityA,
                capacityB,
            )
            == output
        )
