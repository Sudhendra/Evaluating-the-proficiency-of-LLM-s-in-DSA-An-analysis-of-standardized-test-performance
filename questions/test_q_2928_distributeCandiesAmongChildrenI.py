import pytest
from q_2928_distributeCandiesAmongChildrenI import Solution


@pytest.mark.parametrize("n, limit, output", [(5, 2, 3), (3, 3, 10)])
class TestSolution:
    def test_distributeCandies(self, n: int, limit: int, output: int):
        sc = Solution()
        assert (
            sc.distributeCandies(
                n,
                limit,
            )
            == output
        )
