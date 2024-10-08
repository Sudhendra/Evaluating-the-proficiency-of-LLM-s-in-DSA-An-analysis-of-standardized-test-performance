import pytest
from q_2763_sumOfImbalanceNumbersOfAllSubarrays import Solution


@pytest.mark.parametrize("nums, output", [([2, 3, 1, 4], 3), ([1, 3, 3, 3, 5], 8)])
class TestSolution:
    def test_sumImbalanceNumbers(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.sumImbalanceNumbers(
                nums,
            )
            == output
        )
