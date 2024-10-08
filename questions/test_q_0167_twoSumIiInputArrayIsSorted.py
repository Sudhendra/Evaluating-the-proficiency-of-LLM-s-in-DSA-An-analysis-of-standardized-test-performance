import pytest
from q_0167_twoSumIiInputArrayIsSorted import Solution


@pytest.mark.parametrize(
    "numbers, target, output",
    [([2, 7, 11, 15], 9, [1, 2]), ([2, 3, 4], 6, [1, 3]), ([-1, 0], -1, [1, 2])],
)
class TestSolution:
    def test_twoSum(self, numbers: List[int], target: int, output: List[int]):
        sc = Solution()
        assert (
            sc.twoSum(
                numbers,
                target,
            )
            == output
        )
