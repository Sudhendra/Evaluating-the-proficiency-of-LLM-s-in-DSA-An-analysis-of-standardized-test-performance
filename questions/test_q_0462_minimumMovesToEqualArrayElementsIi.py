import pytest
from q_0462_minimumMovesToEqualArrayElementsIi import Solution


@pytest.mark.parametrize("nums, output", [([1, 2, 3], 2), ([1, 10, 2, 9], 16)])
class TestSolution:
    def test_minMoves2(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minMoves2(
                nums,
            )
            == output
        )
