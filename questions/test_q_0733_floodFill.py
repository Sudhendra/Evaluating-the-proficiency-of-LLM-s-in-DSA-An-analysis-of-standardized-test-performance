import pytest
from q_0733_floodFill import Solution


@pytest.mark.parametrize(
    "image, sr, sc, color, output",
    [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]),
    ],
)
class TestSolution:
    def test_floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int,
        output: List[List[int]],
    ):
        sc = Solution()
        assert (
            sc.floodFill(
                image,
                sr,
                sc,
                color,
            )
            == output
        )
