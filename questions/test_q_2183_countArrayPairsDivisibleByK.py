import pytest
from q_2183_countArrayPairsDivisibleByK import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 2, 3, 4, 5], 2, 7), ([1, 2, 3, 4], 5, 0)]
)
class TestSolution:
    def test_countPairs(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.countPairs(
                nums,
                k,
            )
            == output
        )
