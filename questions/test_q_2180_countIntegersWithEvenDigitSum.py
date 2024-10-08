import pytest
from q_2180_countIntegersWithEvenDigitSum import Solution


@pytest.mark.parametrize("num, output", [(4, 2), (30, 14)])
class TestSolution:
    def test_countEven(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.countEven(
                num,
            )
            == output
        )
