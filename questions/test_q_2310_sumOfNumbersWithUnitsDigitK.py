import pytest
from q_2310_sumOfNumbersWithUnitsDigitK import Solution


@pytest.mark.parametrize("num, k, output", [(58, 9, 2), (37, 2, -1), (0, 7, 0)])
class TestSolution:
    def test_minimumNumbers(self, num: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.minimumNumbers(
                num,
                k,
            )
            == output
        )
