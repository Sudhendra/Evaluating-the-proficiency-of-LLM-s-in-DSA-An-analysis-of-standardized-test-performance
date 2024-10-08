import pytest
from q_1387_sortIntegersByThePowerValue import Solution


@pytest.mark.parametrize("lo, hi, k, output", [(12, 15, 2, 13), (7, 11, 4, 7)])
class TestSolution:
    def test_getKth(self, lo: int, hi: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.getKth(
                lo,
                hi,
                k,
            )
            == output
        )
