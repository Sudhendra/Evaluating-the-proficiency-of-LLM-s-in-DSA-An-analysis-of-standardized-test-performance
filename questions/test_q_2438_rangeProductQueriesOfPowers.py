import pytest
from q_2438_rangeProductQueriesOfPowers import Solution


@pytest.mark.parametrize(
    "n, queries, output",
    [(15, [[0, 1], [2, 2], [0, 3]], [2, 4, 64]), (2, [[0, 0]], [2])],
)
class TestSolution:
    def test_productQueries(self, n: int, queries: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.productQueries(
                n,
                queries,
            )
            == output
        )
