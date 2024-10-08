import pytest
from q_0788_rotatedDigits import Solution


@pytest.mark.parametrize("n, output", [(10, 4), (1, 0), (2, 1)])
class TestSolution:
    def test_rotatedDigits(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.rotatedDigits(
                n,
            )
            == output
        )
