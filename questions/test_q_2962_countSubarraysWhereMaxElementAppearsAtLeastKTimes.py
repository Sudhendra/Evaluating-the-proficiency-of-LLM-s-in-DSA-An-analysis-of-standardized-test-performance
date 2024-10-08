import pytest
from q_2962_countSubarraysWhereMaxElementAppearsAtLeastKTimes import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 3, 2, 3, 3], 2, 6), ([1, 4, 2, 1], 3, 0)]
)
class TestSolution:
    def test_countSubarrays(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.countSubarrays(
                nums,
                k,
            )
            == output
        )
