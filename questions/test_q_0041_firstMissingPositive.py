import pytest
from q_0041_firstMissingPositive import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 0], 3), ([3, 4, -1, 1], 2), ([7, 8, 9, 11, 12], 1)]
)
class TestSolution:
    def test_firstMissingPositive(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.firstMissingPositive(
                nums,
            )
            == output
        )
