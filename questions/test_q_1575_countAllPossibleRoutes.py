import pytest
from q_1575_countAllPossibleRoutes import Solution


@pytest.mark.parametrize(
    "locations, start, finish, fuel, output",
    [([2, 3, 6, 8, 4], 1, 3, 5, 4), ([4, 3, 1], 1, 0, 6, 5), ([5, 2, 1], 0, 2, 3, 0)],
)
class TestSolution:
    def test_countRoutes(
        self, locations: List[int], start: int, finish: int, fuel: int, output: int
    ):
        sc = Solution()
        assert (
            sc.countRoutes(
                locations,
                start,
                finish,
                fuel,
            )
            == output
        )
