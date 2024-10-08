import pytest
from q_1855_maximumDistanceBetweenAPairOfValues import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        ([55, 30, 5, 4, 2], [100, 20, 10, 10, 5], 2),
        ([2, 2, 2], [10, 10, 1], 1),
        ([30, 29, 19, 5], [25, 25, 25, 25, 25], 2),
    ],
)
class TestSolution:
    def test_maxDistance(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxDistance(
                nums1,
                nums2,
            )
            == output
        )
