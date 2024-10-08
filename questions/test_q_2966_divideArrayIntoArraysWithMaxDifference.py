import pytest
from q_2966_divideArrayIntoArraysWithMaxDifference import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([1, 3, 4, 8, 7, 9, 3, 5, 1], 2, [[1, 1, 3], [3, 4, 5], [7, 8, 9]]),
        ([1, 3, 3, 2, 7, 3], 3, []),
    ],
)
class TestSolution:
    def test_divideArray(self, nums: List[int], k: int, output: List[List[int]]):
        sc = Solution()
        assert (
            sc.divideArray(
                nums,
                k,
            )
            == output
        )
