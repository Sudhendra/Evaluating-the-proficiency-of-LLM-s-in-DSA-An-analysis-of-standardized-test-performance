import pytest
from q_0738_monotoneIncreasingDigits import Solution


@pytest.mark.parametrize("n, output", [(10, 9), (1234, 1234), (332, 299)])
class TestSolution:
    def test_monotoneIncreasingDigits(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.monotoneIncreasingDigits(
                n,
            )
            == output
        )
