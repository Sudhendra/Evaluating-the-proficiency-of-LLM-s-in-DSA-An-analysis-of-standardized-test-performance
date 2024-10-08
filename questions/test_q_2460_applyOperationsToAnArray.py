import pytest
from q_2460_applyOperationsToAnArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 2, 1, 1, 0], [1, 4, 2, 0, 0, 0]), ([0, 1], [1, 0])]
)
class TestSolution:
    def test_applyOperations(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.applyOperations(
                nums,
            )
            == output
        )
