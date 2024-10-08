import pytest
from q_1295_findNumbersWithEvenNumberOfDigits import Solution


@pytest.mark.parametrize(
    "nums, output", [([12, 345, 2, 6, 7896], 2), ([555, 901, 482, 1771], 1)]
)
class TestSolution:
    def test_findNumbers(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findNumbers(
                nums,
            )
            == output
        )
