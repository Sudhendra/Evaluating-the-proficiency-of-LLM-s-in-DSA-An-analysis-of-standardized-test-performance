import pytest
from q_0645_setMismatch import Solution


@pytest.mark.parametrize("nums, output", [([1, 2, 2, 4], [2, 3]), ([1, 1], [1, 2])])
class TestSolution:
    def test_findErrorNums(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.findErrorNums(
                nums,
            )
            == output
        )
