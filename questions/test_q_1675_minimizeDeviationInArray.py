import pytest
from q_1675_minimizeDeviationInArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 4], 1), ([4, 1, 5, 20, 3], 3), ([2, 10, 8], 3)]
)
class TestSolution:
    def test_minimumDeviation(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumDeviation(
                nums,
            )
            == output
        )
