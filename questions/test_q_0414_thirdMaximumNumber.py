import pytest
from q_0414_thirdMaximumNumber import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 2, 1], 1), ([1, 2], 2), ([2, 2, 3, 1], 1)]
)
class TestSolution:
    def test_thirdMax(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.thirdMax(
                nums,
            )
            == output
        )
