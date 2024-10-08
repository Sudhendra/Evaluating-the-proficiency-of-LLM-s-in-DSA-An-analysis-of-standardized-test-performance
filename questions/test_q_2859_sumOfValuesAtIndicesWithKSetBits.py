import pytest
from q_2859_sumOfValuesAtIndicesWithKSetBits import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([5, 10, 1, 5, 2], 1, 13), ([4, 3, 2, 1], 2, 1)]
)
class TestSolution:
    def test_sumIndicesWithKSetBits(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.sumIndicesWithKSetBits(
                nums,
                k,
            )
            == output
        )
