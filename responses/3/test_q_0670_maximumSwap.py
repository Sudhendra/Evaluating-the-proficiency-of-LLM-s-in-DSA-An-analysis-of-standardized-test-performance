import pytest
from q_0670_maximumSwap import Solution


@pytest.mark.parametrize("num, output", [(2736, 7236), (9973, 9973)])
class TestSolution:
    def test_maximumSwap(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.maximumSwap(
                num,
            )
            == output
        )
