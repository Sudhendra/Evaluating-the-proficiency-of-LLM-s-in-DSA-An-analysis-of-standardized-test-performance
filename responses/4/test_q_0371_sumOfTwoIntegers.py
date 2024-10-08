import pytest
from q_0371_sumOfTwoIntegers import Solution


@pytest.mark.parametrize("a, b, output", [(1, 2, 3), (2, 3, 5)])
class TestSolution:
    def test_getSum(self, a: int, b: int, output: int):
        sc = Solution()
        assert (
            sc.getSum(
                a,
                b,
            )
            == output
        )
