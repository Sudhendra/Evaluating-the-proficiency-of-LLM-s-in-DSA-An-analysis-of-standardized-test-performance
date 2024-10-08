import pytest
from q_1413_minimumValueToGetPositiveStepByStepSum import Solution


@pytest.mark.parametrize(
    "nums, output", [([-3, 2, -3, 4, 2], 5), ([1, 2], 1), ([1, -2, -3], 5)]
)
class TestSolution:
    def test_minStartValue(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minStartValue(
                nums,
            )
            == output
        )
