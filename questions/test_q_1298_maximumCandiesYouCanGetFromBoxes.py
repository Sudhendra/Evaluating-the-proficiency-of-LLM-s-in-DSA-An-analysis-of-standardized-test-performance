import pytest
from q_1298_maximumCandiesYouCanGetFromBoxes import Solution


@pytest.mark.parametrize(
    "status, candies, keys, containedBoxes, initialBoxes, output",
    [
        (
            [1, 0, 1, 0],
            [7, 5, 4, 100],
            [[], [], [1], []],
            [[1, 2], [3], [], []],
            [0],
            16,
        ),
        (
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [[1, 2, 3, 4, 5], [], [], [], [], []],
            [[1, 2, 3, 4, 5], [], [], [], [], []],
            [0],
            6,
        ),
    ],
)
class TestSolution:
    def test_maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
        output: int,
    ):
        sc = Solution()
        assert (
            sc.maxCandies(
                status,
                candies,
                keys,
                containedBoxes,
                initialBoxes,
            )
            == output
        )
