import pytest
from q_1971_findIfPathExistsInGraph import Solution


@pytest.mark.parametrize(
    "n, edges, source, destination, output",
    [
        (3, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5, False),
    ],
)
class TestSolution:
    def test_validPath(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
        output: bool,
    ):
        sc = Solution()
        assert (
            sc.validPath(
                n,
                edges,
                source,
                destination,
            )
            == output
        )
