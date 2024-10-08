import pytest
from q_0805_splitArrayWithSameAverage import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 4, 5, 6, 7, 8], True), ([3, 1], False)]
)
class TestSolution:
    def test_splitArraySameAverage(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.splitArraySameAverage(
                nums,
            )
            == output
        )
