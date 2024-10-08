import pytest
from q_2012_sumOfBeautyInTheArray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3], 2), ([2, 4, 6, 4], 1), ([3, 2, 1], 0)]
)
class TestSolution:
    def test_sumOfBeauties(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.sumOfBeauties(
                nums,
            )
            == output
        )
