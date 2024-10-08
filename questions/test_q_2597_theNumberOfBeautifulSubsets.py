import pytest
from q_2597_theNumberOfBeautifulSubsets import Solution


@pytest.mark.parametrize("nums, k, output", [([2, 4, 6], 2, 4), ([1], 1, 1)])
class TestSolution:
    def test_beautifulSubsets(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.beautifulSubsets(
                nums,
                k,
            )
            == output
        )
