import pytest
from q_0475_heaters import Solution


@pytest.mark.parametrize(
    "houses, heaters, output",
    [([1, 2, 3], [2], 1), ([1, 2, 3, 4], [1, 4], 1), ([1, 5], [2], 3)],
)
class TestSolution:
    def test_findRadius(self, houses: List[int], heaters: List[int], output: int):
        sc = Solution()
        assert (
            sc.findRadius(
                houses,
                heaters,
            )
            == output
        )
