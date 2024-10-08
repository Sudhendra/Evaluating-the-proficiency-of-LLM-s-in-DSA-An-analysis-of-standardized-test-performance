import pytest
from q_0982_triplesWithBitwiseAndEqualToZero import Solution


@pytest.mark.parametrize("nums, output", [([2, 1, 3], 12), ([0, 0, 0], 27)])
class TestSolution:
    def test_countTriplets(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countTriplets(
                nums,
            )
            == output
        )
