import pytest
from q_2848_pointsThatIntersectWithCars import Solution


@pytest.mark.parametrize(
    "nums, output", [([[3, 6], [1, 5], [4, 7]], 7), ([[1, 3], [5, 8]], 7)]
)
class TestSolution:
    def test_numberOfPoints(self, nums: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.numberOfPoints(
                nums,
            )
            == output
        )
