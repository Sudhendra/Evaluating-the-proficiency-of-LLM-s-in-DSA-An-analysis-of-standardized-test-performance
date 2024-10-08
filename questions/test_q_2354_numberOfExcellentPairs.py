import pytest
from q_2354_numberOfExcellentPairs import Solution


@pytest.mark.parametrize("nums, k, output", [([1, 2, 3, 1], 3, 5), ([5, 1, 1], 10, 0)])
class TestSolution:
    def test_countExcellentPairs(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.countExcellentPairs(
                nums,
                k,
            )
            == output
        )
