import pytest
from q_2809_minimumTimeToMakeArraySumAtMostX import Solution


@pytest.mark.parametrize(
    "nums1, nums2, x, output",
    [([1, 2, 3], [1, 2, 3], 4, 3), ([1, 2, 3], [3, 3, 3], 4, -1)],
)
class TestSolution:
    def test_minimumTime(self, nums1: List[int], nums2: List[int], x: int, output: int):
        sc = Solution()
        assert (
            sc.minimumTime(
                nums1,
                nums2,
                x,
            )
            == output
        )
