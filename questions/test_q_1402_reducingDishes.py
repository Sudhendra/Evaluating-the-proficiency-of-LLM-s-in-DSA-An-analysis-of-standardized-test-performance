import pytest
from q_1402_reducingDishes import Solution


@pytest.mark.parametrize(
    "satisfaction, output",
    [([-1, -8, 0, 5, -9], 14), ([4, 3, 2], 20), ([-1, -4, -5], 0)],
)
class TestSolution:
    def test_maxSatisfaction(self, satisfaction: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxSatisfaction(
                satisfaction,
            )
            == output
        )
