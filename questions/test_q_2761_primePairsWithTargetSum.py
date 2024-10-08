import pytest
from q_2761_primePairsWithTargetSum import Solution


@pytest.mark.parametrize("n, output", [(10, [[3, 7], [5, 5]]), (2, [])])
class TestSolution:
    def test_findPrimePairs(self, n: int, output: List[List[int]]):
        sc = Solution()
        assert (
            sc.findPrimePairs(
                n,
            )
            == output
        )
