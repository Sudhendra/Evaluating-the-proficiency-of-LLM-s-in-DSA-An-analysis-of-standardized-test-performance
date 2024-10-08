import pytest
from q_2568_minimumImpossibleOr import Solution


@pytest.mark.parametrize("nums, output", [([2, 1], 4), ([5, 3, 2], 1)])
class TestSolution:
    def test_minImpossibleOR(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minImpossibleOR(
                nums,
            )
            == output
        )
