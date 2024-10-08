import pytest
from q_0672_bulbSwitcherIi import Solution


@pytest.mark.parametrize("n, presses, output", [(1, 1, 2), (2, 1, 3), (3, 1, 4)])
class TestSolution:
    def test_flipLights(self, n: int, presses: int, output: int):
        sc = Solution()
        assert (
            sc.flipLights(
                n,
                presses,
            )
            == output
        )
