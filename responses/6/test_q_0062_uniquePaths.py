import pytest
from q_0062_uniquePaths import Solution


@pytest.mark.parametrize("m, n, output", [(3, 7, 28), (3, 2, 3)])
class TestSolution:
    def test_uniquePaths(self, m: int, n: int, output: int):
        sc = Solution()
        assert (
            sc.uniquePaths(
                m,
                n,
            )
            == output
        )
