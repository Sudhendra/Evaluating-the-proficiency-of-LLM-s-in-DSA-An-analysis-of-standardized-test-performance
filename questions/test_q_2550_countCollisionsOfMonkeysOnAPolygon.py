import pytest
from q_2550_countCollisionsOfMonkeysOnAPolygon import Solution


@pytest.mark.parametrize("n, output", [(3, 6), (4, 14)])
class TestSolution:
    def test_monkeyMove(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.monkeyMove(
                n,
            )
            == output
        )
