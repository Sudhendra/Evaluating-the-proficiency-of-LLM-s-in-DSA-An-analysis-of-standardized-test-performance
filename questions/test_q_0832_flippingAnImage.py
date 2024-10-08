import pytest
from q_0832_flippingAnImage import Solution


@pytest.mark.parametrize(
    "image, output",
    [
        ([[1, 1, 0], [1, 0, 1], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [1, 1, 1]]),
        (
            [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
            [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]],
        ),
    ],
)
class TestSolution:
    def test_flipAndInvertImage(self, image: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.flipAndInvertImage(
                image,
            )
            == output
        )
