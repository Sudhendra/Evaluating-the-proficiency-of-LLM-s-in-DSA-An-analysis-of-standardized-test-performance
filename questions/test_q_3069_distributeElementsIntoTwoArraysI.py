import pytest
from q_3069_distributeElementsIntoTwoArraysI import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 1, 3], [2, 3, 1]), ([5, 4, 3, 8], [5, 3, 4, 8])]
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
