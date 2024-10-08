import pytest
from q_1744_canYouEatYourFavoriteCandyOnYourFavoriteDay import Solution


@pytest.mark.parametrize(
    "candiesCount, queries, output",
    [
        (
            [7, 4, 5, 3, 8],
            [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]],
            [True, False, True],
        ),
        (
            [5, 2, 6, 4, 1],
            [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]],
            [False, True, True, False, False],
        ),
    ],
)
class TestSolution:
    def test_canEat(
        self, candiesCount: List[int], queries: List[List[int]], output: List[bool]
    ):
        sc = Solution()
        assert (
            sc.canEat(
                candiesCount,
                queries,
            )
            == output
        )
