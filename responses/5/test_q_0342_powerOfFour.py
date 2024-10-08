import pytest
from q_0342_powerOfFour import Solution


@pytest.mark.parametrize("n, output", [(16, True), (5, False), (1, True)])
class TestSolution:
    def test_isPowerOfFour(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.isPowerOfFour(
                n,
            )
            == output
        )
