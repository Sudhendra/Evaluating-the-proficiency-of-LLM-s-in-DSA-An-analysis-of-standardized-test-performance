import pytest
from q_1465_maximumAreaOfAPieceOfCakeAfterHorizontalAndVerticalCuts import Solution


@pytest.mark.parametrize(
    "h, w, horizontalCuts, verticalCuts, output",
    [(5, 4, [1, 2, 4], [1, 3], 4), (5, 4, [3, 1], [1], 6), (5, 4, [3], [3], 9)],
)
class TestSolution:
    def test_maxArea(
        self,
        h: int,
        w: int,
        horizontalCuts: List[int],
        verticalCuts: List[int],
        output: int,
    ):
        sc = Solution()
        assert (
            sc.maxArea(
                h,
                w,
                horizontalCuts,
                verticalCuts,
            )
            == output
        )
