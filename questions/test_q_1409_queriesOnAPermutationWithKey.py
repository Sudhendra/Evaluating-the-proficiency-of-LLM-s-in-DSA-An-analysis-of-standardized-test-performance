import pytest
from q_1409_queriesOnAPermutationWithKey import Solution


@pytest.mark.parametrize(
    "queries, m, output",
    [
        ([3, 1, 2, 1], 5, [2, 1, 2, 1]),
        ([4, 1, 2, 2], 4, [3, 1, 2, 0]),
        ([7, 5, 5, 8, 3], 8, [6, 5, 0, 7, 5]),
    ],
)
class TestSolution:
    def test_processQueries(self, queries: List[int], m: int, output: List[int]):
        sc = Solution()
        assert (
            sc.processQueries(
                queries,
                m,
            )
            == output
        )
