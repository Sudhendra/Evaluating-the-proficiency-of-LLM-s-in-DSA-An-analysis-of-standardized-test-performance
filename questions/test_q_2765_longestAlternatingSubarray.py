import pytest
from q_2765_longestAlternatingSubarray import Solution


@pytest.mark.parametrize("nums, output", [([2, 3, 4, 3, 4], 4), ([4, 5, 6], 2)])
class TestSolution:
    def test_alternatingSubarray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.alternatingSubarray(
                nums,
            )
            == output
        )
