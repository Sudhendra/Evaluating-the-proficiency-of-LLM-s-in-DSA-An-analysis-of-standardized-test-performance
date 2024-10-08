import pytest
from q_0718_maximumLengthOfRepeatedSubarray import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [([1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3), ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 5)],
)
class TestSolution:
    def test_findLength(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.findLength(
                nums1,
                nums2,
            )
            == output
        )
