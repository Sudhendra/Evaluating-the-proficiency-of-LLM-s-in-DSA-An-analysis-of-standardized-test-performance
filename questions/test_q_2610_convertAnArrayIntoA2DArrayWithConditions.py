import pytest
from q_2610_convertAnArrayIntoA2DArrayWithConditions import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 3, 4, 1, 2, 3, 1], [[1, 3, 4, 2], [1, 3], [1]]),
        ([1, 2, 3, 4], [[4, 3, 2, 1]]),
    ],
)
class TestSolution:
    def test_findMatrix(self, nums: List[int], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.findMatrix(
                nums,
            )
            == output
        )
