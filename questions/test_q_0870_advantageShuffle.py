import pytest
from q_0870_advantageShuffle import Solution


@pytest.mark.parametrize(
    "nums1, nums2, output",
    [
        ([2, 7, 11, 15], [1, 10, 4, 11], [2, 11, 7, 15]),
        ([12, 24, 8, 32], [13, 25, 32, 11], [24, 32, 8, 12]),
    ],
)
class TestSolution:
    def test_advantageCount(
        self, nums1: List[int], nums2: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.advantageCount(
                nums1,
                nums2,
            )
            == output
        )
