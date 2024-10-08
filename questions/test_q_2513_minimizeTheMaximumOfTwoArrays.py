import pytest
from q_2513_minimizeTheMaximumOfTwoArrays import Solution


@pytest.mark.parametrize(
    "divisor1, divisor2, uniqueCnt1, uniqueCnt2, output",
    [(2, 7, 1, 3, 4), (3, 5, 2, 1, 3), (2, 4, 8, 2, 15)],
)
class TestSolution:
    def test_minimizeSet(
        self,
        divisor1: int,
        divisor2: int,
        uniqueCnt1: int,
        uniqueCnt2: int,
        output: int,
    ):
        sc = Solution()
        assert (
            sc.minimizeSet(
                divisor1,
                divisor2,
                uniqueCnt1,
                uniqueCnt2,
            )
            == output
        )
