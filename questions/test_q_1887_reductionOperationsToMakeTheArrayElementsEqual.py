import pytest
from q_1887_reductionOperationsToMakeTheArrayElementsEqual import Solution


@pytest.mark.parametrize(
    "nums, output", [([5, 1, 3], 3), ([1, 1, 1], 0), ([1, 1, 2, 2, 3], 4)]
)
class TestSolution:
    def test_reductionOperations(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.reductionOperations(
                nums,
            )
            == output
        )
