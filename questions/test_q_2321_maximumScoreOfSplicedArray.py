import pytest
from q_2321_maximumScoreOfSplicedArray import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        ([60, 60, 60], [10, 90, 10], 210),
        ([20, 40, 20, 70, 30], [50, 20, 50, 40, 20], 220),
        ([7, 11, 13], [1, 1, 1], 31),
    ],
)
class TestSolution:
    def test_maximumsSplicedArray(
        self, nums1: List[int], nums2: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.maximumsSplicedArray(
                nums1,
                nums2,
            )
            == output
        )
