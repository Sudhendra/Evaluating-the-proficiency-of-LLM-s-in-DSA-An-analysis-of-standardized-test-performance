import pytest
from q_0421_maximumXorOfTwoNumbersInAnArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([3, 10, 5, 25, 2, 8], 28),
        ([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70], 127),
    ],
)
class TestSolution:
    def test_findMaximumXOR(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findMaximumXOR(
                nums,
            )
            == output
        )
