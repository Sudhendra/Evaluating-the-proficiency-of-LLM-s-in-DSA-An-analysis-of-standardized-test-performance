import pytest
from q_0976_largestPerimeterTriangle import Solution


@pytest.mark.parametrize("nums, output", [([2, 1, 2], 5), ([1, 2, 1, 10], 0)])
class TestSolution:
    def test_largestPerimeter(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.largestPerimeter(
                nums,
            )
            == output
        )
