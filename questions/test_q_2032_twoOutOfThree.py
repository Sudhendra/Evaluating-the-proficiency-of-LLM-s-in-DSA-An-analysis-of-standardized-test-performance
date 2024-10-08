import pytest
from q_2032_twoOutOfThree import Solution


@pytest.mark.parametrize(
    "nums1, nums2, nums3, output",
    [
        ([1, 1, 3, 2], [2, 3], [3], [3, 2]),
        ([3, 1], [2, 3], [1, 2], [2, 3, 1]),
        ([1, 2, 2], [4, 3, 3], [5], []),
    ],
)
class TestSolution:
    def test_twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.twoOutOfThree(
                nums1,
                nums2,
                nums3,
            )
            == output
        )
