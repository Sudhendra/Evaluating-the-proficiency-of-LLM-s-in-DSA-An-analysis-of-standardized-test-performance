import pytest
from q_2364_countNumberOfBadPairs import Solution


@pytest.mark.parametrize("nums, output", [([4, 1, 3, 3], 5), ([1, 2, 3, 4, 5], 0)])
class TestSolution:
    def test_countBadPairs(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countBadPairs(
                nums,
            )
            == output
        )
