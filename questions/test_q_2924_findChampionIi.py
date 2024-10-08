import pytest
from q_2924_findChampionIi import Solution


@pytest.mark.parametrize(
    "n, edges, output", [(3, [[0, 1], [1, 2]], 0), (4, [[0, 2], [1, 3], [1, 2]], -1)]
)
class TestSolution:
    def test_findChampion(self, n: int, edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.findChampion(
                n,
                edges,
            )
            == output
        )
