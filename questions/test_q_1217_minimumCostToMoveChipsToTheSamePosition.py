import pytest
from q_1217_minimumCostToMoveChipsToTheSamePosition import Solution


@pytest.mark.parametrize(
    "position, output", [([1, 2, 3], 1), ([2, 2, 2, 3, 3], 2), ([1, 1000000000], 1)]
)
class TestSolution:
    def test_minCostToMoveChips(self, position: List[int], output: int):
        sc = Solution()
        assert (
            sc.minCostToMoveChips(
                position,
            )
            == output
        )
