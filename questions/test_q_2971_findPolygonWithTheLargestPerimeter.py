import pytest
from q_2971_findPolygonWithTheLargestPerimeter import Solution


@pytest.mark.parametrize(
    "nums, output", [([5, 5, 5], 15), ([1, 12, 1, 2, 5, 50, 3], 12), ([5, 5, 50], -1)]
)
class TestSolution:
    def test_largestPerimeter(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.largestPerimeter(
                nums,
            )
            == output
        )
