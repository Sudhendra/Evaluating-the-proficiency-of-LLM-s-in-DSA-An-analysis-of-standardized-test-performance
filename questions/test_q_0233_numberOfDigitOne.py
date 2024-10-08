import pytest
from q_0233_numberOfDigitOne import Solution


@pytest.mark.parametrize("n, output", [(13, 6), (0, 0)])
class TestSolution:
    def test_countDigitOne(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.countDigitOne(
                n,
            )
            == output
        )
