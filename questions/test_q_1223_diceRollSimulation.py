import pytest
from q_1223_diceRollSimulation import Solution


@pytest.mark.parametrize(
    "n, rollMax, output",
    [
        (2, [1, 1, 2, 2, 2, 3], 34),
        (2, [1, 1, 1, 1, 1, 1], 30),
        (3, [1, 1, 1, 2, 2, 3], 181),
    ],
)
class TestSolution:
    def test_dieSimulator(self, n: int, rollMax: List[int], output: int):
        sc = Solution()
        assert (
            sc.dieSimulator(
                n,
                rollMax,
            )
            == output
        )
