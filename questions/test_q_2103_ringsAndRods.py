import pytest
from q_2103_ringsAndRods import Solution


@pytest.mark.parametrize(
    "rings, output", [("B0B6G0R6R0R6G9", 1), ("B0R0G0R9R0B0G0", 1), ("G4", 0)]
)
class TestSolution:
    def test_countPoints(self, rings: str, output: int):
        sc = Solution()
        assert (
            sc.countPoints(
                rings,
            )
            == output
        )
