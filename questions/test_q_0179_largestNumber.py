import pytest
from q_0179_largestNumber import Solution


@pytest.mark.parametrize(
    "nums, output", [([10, 2], "210"), ([3, 30, 34, 5, 9], "9534330")]
)
class TestSolution:
    def test_largestNumber(self, nums: List[int], output: str):
        sc = Solution()
        assert (
            sc.largestNumber(
                nums,
            )
            == output
        )
