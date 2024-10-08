import pytest
from q_1847_closestRoom import Solution


@pytest.mark.parametrize(
    "rooms, queries, output",
    [
        ([[2, 2], [1, 2], [3, 2]], [[3, 1], [3, 3], [5, 2]], [3, -1, 3]),
        ([[1, 4], [2, 3], [3, 5], [4, 1], [5, 2]], [[2, 3], [2, 4], [2, 5]], [2, 1, 3]),
    ],
)
class TestSolution:
    def test_closestRoom(
        self, rooms: List[List[int]], queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.closestRoom(
                rooms,
                queries,
            )
            == output
        )
