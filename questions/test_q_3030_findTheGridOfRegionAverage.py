import pytest
from q_3030_findTheGridOfRegionAverage import Solution


@pytest.mark.parametrize(
    "image, threshold, output",
    [
        (
            [[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]],
            3,
            [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]],
        ),
        (
            [[10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]],
            12,
            [[25, 25, 25], [27, 27, 27], [27, 27, 27], [30, 30, 30]],
        ),
        (
            [[5, 6, 7], [8, 9, 10], [11, 12, 13]],
            1,
            [[5, 6, 7], [8, 9, 10], [11, 12, 13]],
        ),
    ],
)
class TestSolution:
    def test_resultGrid(
        self, image: List[List[int]], threshold: int, output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.resultGrid(
                image,
                threshold,
            )
            == output
        )
