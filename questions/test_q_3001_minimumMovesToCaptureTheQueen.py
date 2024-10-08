import pytest
from q_3001_minimumMovesToCaptureTheQueen import Solution


@pytest.mark.parametrize(
    "a, b, c, d, e, f, output", [(1, 1, 8, 8, 2, 3, 2), (5, 3, 3, 4, 5, 2, 1)]
)
class TestSolution:
    def test_minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int, output: int
    ):
        sc = Solution()
        assert (
            sc.minMovesToCaptureTheQueen(
                a,
                b,
                c,
                d,
                e,
                f,
            )
            == output
        )
