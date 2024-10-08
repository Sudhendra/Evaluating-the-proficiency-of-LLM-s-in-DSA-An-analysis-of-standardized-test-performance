import pytest
from q_2742_paintingTheWalls import Solution


@pytest.mark.parametrize(
    "cost, time, output",
    [([1, 2, 3, 2], [1, 2, 3, 2], 3), ([2, 3, 4, 2], [1, 1, 1, 1], 4)],
)
class TestSolution:
    def test_paintWalls(self, cost: List[int], time: List[int], output: int):
        sc = Solution()
        assert (
            sc.paintWalls(
                cost,
                time,
            )
            == output
        )
