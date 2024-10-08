import pytest
from q_2681_powerOfHeroes import Solution


@pytest.mark.parametrize("nums, output", [([2, 1, 4], 141), ([1, 1, 1], 7)])
class TestSolution:
    def test_sumOfPower(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.sumOfPower(
                nums,
            )
            == output
        )
