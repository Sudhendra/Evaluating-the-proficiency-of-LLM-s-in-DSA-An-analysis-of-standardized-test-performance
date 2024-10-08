import pytest
from q_2439_minimizeMaximumOfArray import Solution


@pytest.mark.parametrize("nums, output", [([3, 7, 1, 6], 5), ([10, 1], 10)])
class TestSolution:
    def test_minimizeArrayValue(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimizeArrayValue(
                nums,
            )
            == output
        )
