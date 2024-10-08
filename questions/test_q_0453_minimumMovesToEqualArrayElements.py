import pytest
from q_0453_minimumMovesToEqualArrayElements import Solution


@pytest.mark.parametrize("nums, output", [([1, 2, 3], 3), ([1, 1, 1], 0)])
class TestSolution:
    def test_minMoves(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minMoves(
                nums,
            )
            == output
        )
