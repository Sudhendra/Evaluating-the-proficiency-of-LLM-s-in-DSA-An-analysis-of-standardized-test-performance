import pytest
from q_2870_minimumNumberOfOperationsToMakeArrayEmpty import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 3, 3, 2, 2, 4, 2, 3, 4], 4), ([2, 1, 2, 2, 3, 3], -1)]
)
class TestSolution:
    def test_minOperations(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums,
            )
            == output
        )
