import pytest
from q_2215_findTheDifferenceOfTwoArrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]), ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []])],
)
class TestSolution:
    def test_findDifference(
        self, nums1: List[int], nums2: List[int], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.findDifference(
                nums1,
                nums2,
            )
            == output
        )
