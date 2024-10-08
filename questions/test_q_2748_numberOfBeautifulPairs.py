import pytest
from q_2748_numberOfBeautifulPairs import Solution


@pytest.mark.parametrize("nums, output", [([2, 5, 1, 4], 5), ([11, 21, 12], 2)])
class TestSolution:
    def test_countBeautifulPairs(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countBeautifulPairs(
                nums,
            )
            == output
        )
