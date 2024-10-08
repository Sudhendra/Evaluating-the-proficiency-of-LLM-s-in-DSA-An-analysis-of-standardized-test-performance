import pytest
from q_1144_decreaseElementsToMakeArrayZigzag import Solution


@pytest.mark.parametrize("nums, output", [([1, 2, 3], 2), ([9, 6, 1, 6, 2], 4)])
class TestSolution:
    def test_movesToMakeZigzag(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.movesToMakeZigzag(
                nums,
            )
            == output
        )
