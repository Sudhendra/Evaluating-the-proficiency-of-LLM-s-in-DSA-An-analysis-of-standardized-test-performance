import pytest
from q_2833_furthestPointFromOrigin import Solution


@pytest.mark.parametrize(
    "moves, output", [("L_RL__R", 3), ("_R__LL_", 5), ("_______", 7)]
)
class TestSolution:
    def test_furthestDistanceFromOrigin(self, moves: str, output: int):
        sc = Solution()
        assert (
            sc.furthestDistanceFromOrigin(
                moves,
            )
            == output
        )
