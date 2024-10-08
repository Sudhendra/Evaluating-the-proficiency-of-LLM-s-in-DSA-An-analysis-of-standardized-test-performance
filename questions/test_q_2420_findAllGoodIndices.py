import pytest
from q_2420_findAllGoodIndices import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([2, 1, 1, 1, 3, 4, 1], 2, [2, 3]), ([2, 1, 1, 2], 2, [])]
)
class TestSolution:
    def test_goodIndices(self, nums: List[int], k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.goodIndices(
                nums,
                k,
            )
            == output
        )
