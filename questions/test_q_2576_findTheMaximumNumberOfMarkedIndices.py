import pytest
from q_2576_findTheMaximumNumberOfMarkedIndices import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 5, 2, 4], 2), ([9, 2, 5, 4], 4), ([7, 6, 8], 0)]
)
class TestSolution:
    def test_maxNumOfMarkedIndices(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxNumOfMarkedIndices(
                nums,
            )
            == output
        )
