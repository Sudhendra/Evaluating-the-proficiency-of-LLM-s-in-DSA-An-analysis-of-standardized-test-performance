import pytest
from q_1879_minimumXorSumOfTwoArrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output", [([1, 2], [2, 3], 2), ([1, 0, 3], [5, 3, 4], 8)]
)
class TestSolution:
    def test_minimumXORSum(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumXORSum(
                nums1,
                nums2,
            )
            == output
        )
