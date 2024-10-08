import pytest
from q_2605_formSmallestNumberFromTwoDigitArrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output", [([4, 1, 3], [5, 7], 15), ([3, 5, 2, 6], [3, 1, 7], 3)]
)
class TestSolution:
    def test_minNumber(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.minNumber(
                nums1,
                nums2,
            )
            == output
        )
