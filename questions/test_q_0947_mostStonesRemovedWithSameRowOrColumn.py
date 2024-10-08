import pytest
from q_0947_mostStonesRemovedWithSameRowOrColumn import Solution


@pytest.mark.parametrize(
    "stones, output",
    [
        ([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]], 5),
        ([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]], 3),
        ([[0, 0]], 0),
    ],
)
class TestSolution:
    def test_removeStones(self, stones: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.removeStones(
                stones,
            )
            == output
        )
