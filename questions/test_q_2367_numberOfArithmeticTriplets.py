import pytest
from q_2367_numberOfArithmeticTriplets import Solution


@pytest.mark.parametrize(
    "nums, diff, output", [([0, 1, 4, 6, 7, 10], 3, 2), ([4, 5, 6, 7, 8, 9], 2, 2)]
)
class TestSolution:
    def test_arithmeticTriplets(self, nums: List[int], diff: int, output: int):
        sc = Solution()
        assert (
            sc.arithmeticTriplets(
                nums,
                diff,
            )
            == output
        )
