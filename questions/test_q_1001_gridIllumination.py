import pytest
from q_1001_gridIllumination import Solution


@pytest.mark.parametrize(
    "n, lamps, queries, output",
    [
        (5, [[0, 0], [4, 4]], [[1, 1], [1, 0]], [1, 0]),
        (5, [[0, 0], [4, 4]], [[1, 1], [1, 1]], [1, 1]),
        (5, [[0, 0], [0, 4]], [[0, 4], [0, 1], [1, 4]], [1, 1, 0]),
    ],
)
class TestSolution:
    def test_gridIllumination(
        self,
        n: int,
        lamps: List[List[int]],
        queries: List[List[int]],
        output: List[int],
    ):
        sc = Solution()
        assert (
            sc.gridIllumination(
                n,
                lamps,
                queries,
            )
            == output
        )
