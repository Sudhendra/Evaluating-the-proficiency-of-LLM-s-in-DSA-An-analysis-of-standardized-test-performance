import pytest
from q_3072_distributeElementsIntoTwoArraysIi import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([2, 1, 3, 3], [2, 3, 1, 3]),
        ([5, 14, 3, 1, 2], [5, 3, 1, 2, 14]),
        ([3, 3, 3, 3], [3, 3, 3, 3]),
    ],
)
class TestSolution:
    def test_resultArray(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.resultArray(
                nums,
            )
            == output
        )
