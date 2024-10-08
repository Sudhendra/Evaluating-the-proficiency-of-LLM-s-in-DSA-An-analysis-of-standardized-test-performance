import pytest
from q_0835_imageOverlap import Solution


@pytest.mark.parametrize(
    "img1, img2, output",
    [
        ([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]], 3),
        ([[1]], [[1]], 1),
        ([[0]], [[0]], 0),
    ],
)
class TestSolution:
    def test_largestOverlap(
        self, img1: List[List[int]], img2: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.largestOverlap(
                img1,
                img2,
            )
            == output
        )
