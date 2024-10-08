import pytest
from q_0910_smallestRangeIi import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1], 0, 0), ([0, 10], 2, 6), ([1, 3, 6], 3, 3)]
)
class TestSolution:
    def test_smallestRangeII(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.smallestRangeII(
                nums,
                k,
            )
            == output
        )
