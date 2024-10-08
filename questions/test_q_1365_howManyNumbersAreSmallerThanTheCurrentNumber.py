import pytest
from q_1365_howManyNumbersAreSmallerThanTheCurrentNumber import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
        ([6, 5, 4, 8], [2, 1, 0, 3]),
        ([7, 7, 7, 7], [0, 0, 0, 0]),
    ],
)
class TestSolution:
    def test_smallerNumbersThanCurrent(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.smallerNumbersThanCurrent(
                nums,
            )
            == output
        )
