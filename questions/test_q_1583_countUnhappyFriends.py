import pytest
from q_1583_countUnhappyFriends import Solution


@pytest.mark.parametrize(
    "n, preferences, pairs, output",
    [
        (4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]], 2),
        (2, [[1], [0]], [[1, 0]], 0),
        (4, [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], [[1, 3], [0, 2]], 4),
    ],
)
class TestSolution:
    def test_unhappyFriends(
        self, n: int, preferences: List[List[int]], pairs: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.unhappyFriends(
                n,
                preferences,
                pairs,
            )
            == output
        )
