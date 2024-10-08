import pytest
from q_0319_bulbSwitcher import Solution


@pytest.mark.parametrize("n, output", [(3, 1), (0, 0), (1, 1)])
class TestSolution:
    def test_bulbSwitch(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.bulbSwitch(
                n,
            )
            == output
        )
