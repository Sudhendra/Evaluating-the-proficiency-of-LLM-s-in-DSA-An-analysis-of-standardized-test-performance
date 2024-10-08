import pytest
from q_0798_smallestRotationWithHighestScore import Solution


@pytest.mark.parametrize("nums, output", [([2, 3, 1, 4, 0], 3), ([1, 3, 0, 2, 4], 0)])
class TestSolution:
    def test_bestRotation(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.bestRotation(
                nums,
            )
            == output
        )
