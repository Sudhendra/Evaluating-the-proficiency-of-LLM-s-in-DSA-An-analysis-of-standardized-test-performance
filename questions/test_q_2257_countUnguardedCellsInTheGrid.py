import pytest
from q_2257_countUnguardedCellsInTheGrid import Solution


@pytest.mark.parametrize(
    "m, n, guards, walls, output",
    [
        (4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]], 7),
        (3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]], 4),
    ],
)
class TestSolution:
    def test_countUnguarded(
        self,
        m: int,
        n: int,
        guards: List[List[int]],
        walls: List[List[int]],
        output: int,
    ):
        sc = Solution()
        assert (
            sc.countUnguarded(
                m,
                n,
                guards,
                walls,
            )
            == output
        )
