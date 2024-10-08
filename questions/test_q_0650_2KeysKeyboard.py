import pytest
from q_0650_2KeysKeyboard import Solution


@pytest.mark.parametrize("n, output", [(3, 3), (1, 0)])
class TestSolution:
    def test_minSteps(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.minSteps(
                n,
            )
            == output
        )
