import pytest
from q_3041_maximizeConsecutiveElementsInAnArrayAfterModification import Solution


@pytest.mark.parametrize("nums, output", [([2, 1, 5, 1, 1], 3), ([1, 4, 7, 10], 1)])
class TestSolution:
    def test_maxSelectedElements(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxSelectedElements(
                nums,
            )
            == output
        )
