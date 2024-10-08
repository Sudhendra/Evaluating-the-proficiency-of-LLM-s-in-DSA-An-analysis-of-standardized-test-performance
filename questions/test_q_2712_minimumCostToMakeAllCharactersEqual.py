import pytest
from q_2712_minimumCostToMakeAllCharactersEqual import Solution


@pytest.mark.parametrize("s, output", [("0011", 2), ("010101", 9)])
class TestSolution:
    def test_minimumCost(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minimumCost(
                s,
            )
            == output
        )
