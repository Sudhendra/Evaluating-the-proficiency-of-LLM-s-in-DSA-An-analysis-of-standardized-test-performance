import pytest
from q_2190_mostFrequentNumberFollowingKeyInAnArray import Solution


@pytest.mark.parametrize(
    "nums, key, output", [([1, 100, 200, 1, 100], 1, 100), ([2, 2, 2, 2, 3], 2, 2)]
)
class TestSolution:
    def test_mostFrequent(self, nums: List[int], key: int, output: int):
        sc = Solution()
        assert (
            sc.mostFrequent(
                nums,
                key,
            )
            == output
        )
