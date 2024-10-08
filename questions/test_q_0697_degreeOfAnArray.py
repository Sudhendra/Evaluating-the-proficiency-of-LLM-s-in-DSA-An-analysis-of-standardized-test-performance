import pytest
from q_0697_degreeOfAnArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 2, 3, 1], 2), ([1, 2, 2, 3, 1, 4, 2], 6)]
)
class TestSolution:
    def test_findShortestSubArray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findShortestSubArray(
                nums,
            )
            == output
        )
