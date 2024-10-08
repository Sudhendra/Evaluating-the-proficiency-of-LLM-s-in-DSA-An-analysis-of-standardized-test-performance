import pytest
from q_2425_bitwiseXorOfAllPairings import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output", [([2, 1, 3], [10, 2, 5, 0], 13), ([1, 2], [3, 4], 0)]
)
class TestSolution:
    def test_xorAllNums(self, nums1: List[int], nums2: List[int], output: int):
        sc = Solution()
        assert (
            sc.xorAllNums(
                nums1,
                nums2,
            )
            == output
        )
