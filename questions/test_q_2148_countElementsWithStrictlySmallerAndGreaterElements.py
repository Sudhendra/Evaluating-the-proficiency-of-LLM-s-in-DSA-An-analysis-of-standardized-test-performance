import pytest
from q_2148_countElementsWithStrictlySmallerAndGreaterElements import Solution


@pytest.mark.parametrize("nums, output", [([11, 7, 2, 15], 2), ([-3, 3, 3, 90], 2)])
class TestSolution:
    def test_countElements(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countElements(
                nums,
            )
            == output
        )
