import pytest
from q_2553_separateTheDigitsInAnArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([13, 25, 83, 77], [1, 3, 2, 5, 8, 3, 7, 7]), ([7, 1, 3, 9], [7, 1, 3, 9])],
)
class TestSolution:
    def test_separateDigits(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.separateDigits(
                nums,
            )
            == output
        )
