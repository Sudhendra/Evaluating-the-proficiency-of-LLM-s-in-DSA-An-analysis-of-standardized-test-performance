import pytest
from q_2831_findTheLongestEqualSubarray import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 3, 2, 3, 1, 3], 3, 3), ([1, 1, 2, 2, 1, 1], 2, 4)]
)
class TestSolution:
    def test_longestEqualSubarray(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.longestEqualSubarray(
                nums,
                k,
            )
            == output
        )
