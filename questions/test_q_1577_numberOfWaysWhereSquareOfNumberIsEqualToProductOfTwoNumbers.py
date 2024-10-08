import pytest
from q_1577_numberOfWaysWhereSquareOfNumberIsEqualToProductOfTwoNumbers import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        ([7, 4], [5, 2, 8, 9], 1),
        ([1, 1], [1, 1, 1], 9),
        ([7, 7, 8, 3], [1, 2, 9, 7], 2),
    ],
)
class TestSolution:
    def test_numTriplets(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.numTriplets(
                nums1,
                nums2,
            )
            == output
        )
