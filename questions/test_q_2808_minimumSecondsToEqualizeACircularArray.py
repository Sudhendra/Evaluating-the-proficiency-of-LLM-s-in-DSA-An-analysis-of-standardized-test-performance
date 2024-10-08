import pytest
from q_2808_minimumSecondsToEqualizeACircularArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 1, 2], 1), ([2, 1, 3, 3, 2], 2), ([5, 5, 5, 5], 0)]
)
class TestSolution:
    def test_minimumSeconds(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumSeconds(
                nums,
            )
            == output
        )
