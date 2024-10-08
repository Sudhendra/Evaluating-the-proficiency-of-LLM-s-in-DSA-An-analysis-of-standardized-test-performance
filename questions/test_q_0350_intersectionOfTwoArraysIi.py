import pytest
from q_0350_intersectionOfTwoArraysIi import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [([1, 2, 2, 1], [2, 2], [2, 2]), ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9])],
)
class TestSolution:
    def test_intersect(self, nums1: List[int], nums2: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.intersect(
                nums1,
                nums2,
            )
            == output
        )
