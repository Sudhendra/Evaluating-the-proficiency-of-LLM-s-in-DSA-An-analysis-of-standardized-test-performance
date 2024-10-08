import pytest
from q_1659_maximizeGridHappiness import Solution


@pytest.mark.parametrize(
    "m, n, introvertsCount, extrovertsCount, output",
    [(2, 3, 1, 2, 240), (3, 1, 2, 1, 260), (2, 2, 4, 0, 240)],
)
class TestSolution:
    def test_getMaxGridHappiness(
        self, m: int, n: int, introvertsCount: int, extrovertsCount: int, output: int
    ):
        sc = Solution()
        assert (
            sc.getMaxGridHappiness(
                m,
                n,
                introvertsCount,
                extrovertsCount,
            )
            == output
        )
