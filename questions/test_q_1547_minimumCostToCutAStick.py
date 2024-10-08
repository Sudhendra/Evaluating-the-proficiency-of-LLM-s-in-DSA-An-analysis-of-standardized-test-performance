import pytest
from q_1547_minimumCostToCutAStick import Solution


@pytest.mark.parametrize(
    "n, cuts, output", [(7, [1, 3, 4, 5], 16), (9, [5, 6, 1, 4, 2], 22)]
)
class TestSolution:
    def test_minCost(self, n: int, cuts: List[int], output: int):
        sc = Solution()
        assert (
            sc.minCost(
                n,
                cuts,
            )
            == output
        )
