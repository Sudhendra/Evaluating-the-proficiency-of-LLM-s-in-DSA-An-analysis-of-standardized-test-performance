import pytest
from q_2147_numberOfWaysToDivideALongCorridor import Solution


@pytest.mark.parametrize("corridor, output", [("SSPPSPS", 3), ("PPSPSP", 1), ("S", 0)])
class TestSolution:
    def test_numberOfWays(self, corridor: str, output: int):
        sc = Solution()
        assert (
            sc.numberOfWays(
                corridor,
            )
            == output
        )
