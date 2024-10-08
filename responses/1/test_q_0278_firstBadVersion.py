import pytest
from q_0278_firstBadVersion import Solution


@pytest.mark.parametrize("n, bad, output", [(5, 4, 4), (1, 1, 1)])
class TestSolution:
    def test_firstBadVersion(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.firstBadVersion(
                n,
                bad,
            )
            == output
        )
