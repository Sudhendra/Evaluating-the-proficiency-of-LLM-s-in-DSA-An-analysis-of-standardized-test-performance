import pytest
from q_0540_singleElementInASortedArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 1, 2, 3, 3, 4, 4, 8, 8], 2), ([3, 3, 7, 7, 10, 11, 11], 10)]
)
class TestSolution:
    def test_singleNonDuplicate(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.singleNonDuplicate(
                nums,
            )
            == output
        )
