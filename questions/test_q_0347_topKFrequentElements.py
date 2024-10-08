import pytest
from q_0347_topKFrequentElements import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 1, 1, 2, 2, 3], 2, [1, 2]), ([1], 1, [1])]
)
class TestSolution:
    def test_topKFrequent(self, nums: List[int], k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.topKFrequent(
                nums,
                k,
            )
            == output
        )
