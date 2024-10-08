import pytest
from q_2588_countTheNumberOfBeautifulSubarrays import Solution


@pytest.mark.parametrize("nums, output", [([4, 3, 1, 2, 4], 2), ([1, 10, 4], 0)])
class TestSolution:
    def test_beautifulSubarrays(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.beautifulSubarrays(
                nums,
            )
            == output
        )
