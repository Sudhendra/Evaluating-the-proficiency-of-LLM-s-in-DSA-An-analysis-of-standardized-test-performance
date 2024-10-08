import pytest
from q_2079_wateringPlants import Solution


@pytest.mark.parametrize(
    "plants, capacity, output",
    [
        ([2, 2, 3, 3], 5, 14),
        ([1, 1, 1, 4, 2, 3], 4, 30),
        ([7, 7, 7, 7, 7, 7, 7], 8, 49),
    ],
)
class TestSolution:
    def test_wateringPlants(self, plants: List[int], capacity: int, output: int):
        sc = Solution()
        assert (
            sc.wateringPlants(
                plants,
                capacity,
            )
            == output
        )
