import pytest
from q_2740_findTheValueOfThePartition import Solution


@pytest.mark.parametrize("nums, output", [([1, 3, 2, 4], 1), ([100, 1, 10], 9)])
class TestSolution:
    def test_findValueOfPartition(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findValueOfPartition(
                nums,
            )
            == output
        )
