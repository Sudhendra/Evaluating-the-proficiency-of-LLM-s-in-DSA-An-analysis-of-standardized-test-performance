import pytest
from q_0120_triangle import Solution


@pytest.mark.parametrize(
    "triangle, output", [([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11), ([[-10]], -10)]
)
class TestSolution:
    def test_minimumTotal(self, triangle: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minimumTotal(
                triangle,
            )
            == output
        )
