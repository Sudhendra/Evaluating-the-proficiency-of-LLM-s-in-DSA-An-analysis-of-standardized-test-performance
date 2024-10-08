import pytest
from q_1411_numberOfWaysToPaintN3Grid import Solution


@pytest.mark.parametrize("n, output", [(1, 12), (5000, 30228214)])
class TestSolution:
    def test_numOfWays(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.numOfWays(
                n,
            )
            == output
        )
