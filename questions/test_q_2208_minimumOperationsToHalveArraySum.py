import pytest
from q_2208_minimumOperationsToHalveArraySum import Solution


@pytest.mark.parametrize("nums, output", [([5, 19, 8, 1], 3), ([3, 8, 20], 3)])
class TestSolution:
    def test_halveArray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.halveArray(
                nums,
            )
            == output
        )
