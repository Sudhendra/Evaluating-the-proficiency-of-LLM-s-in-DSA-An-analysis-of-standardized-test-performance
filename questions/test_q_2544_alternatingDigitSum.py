import pytest
from q_2544_alternatingDigitSum import Solution


@pytest.mark.parametrize("n, output", [(521, 4), (111, 1), (886996, 0)])
class TestSolution:
    def test_alternateDigitSum(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.alternateDigitSum(
                n,
            )
            == output
        )
