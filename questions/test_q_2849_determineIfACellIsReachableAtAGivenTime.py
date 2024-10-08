import pytest
from q_2849_determineIfACellIsReachableAtAGivenTime import Solution


@pytest.mark.parametrize(
    "sx, sy, fx, fy, t, output", [(2, 4, 7, 7, 6, True), (3, 1, 7, 3, 3, False)]
)
class TestSolution:
    def test_isReachableAtTime(
        self, sx: int, sy: int, fx: int, fy: int, t: int, output: bool
    ):
        sc = Solution()
        assert (
            sc.isReachableAtTime(
                sx,
                sy,
                fx,
                fy,
                t,
            )
            == output
        )
