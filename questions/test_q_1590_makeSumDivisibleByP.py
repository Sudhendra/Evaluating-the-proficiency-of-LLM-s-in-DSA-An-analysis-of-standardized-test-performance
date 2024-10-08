import pytest
from q_1590_makeSumDivisibleByP import Solution


@pytest.mark.parametrize(
    "nums, p, output", [([3, 1, 4, 2], 6, 1), ([6, 3, 5, 2], 9, 2), ([1, 2, 3], 3, 0)]
)
class TestSolution:
    def test_minSubarray(self, nums: List[int], p: int, output: int):
        sc = Solution()
        assert (
            sc.minSubarray(
                nums,
                p,
            )
            == output
        )
