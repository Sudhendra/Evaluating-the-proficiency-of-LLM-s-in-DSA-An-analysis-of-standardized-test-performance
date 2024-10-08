import pytest
from q_2455_averageValueOfEvenNumbersThatAreDivisibleByThree import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 3, 6, 10, 12, 15], 9), ([1, 2, 4, 7, 10], 0)]
)
class TestSolution:
    def test_averageValue(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.averageValue(
                nums,
            )
            == output
        )
