import pytest
from q_0268_missingNumber import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 0, 1], 2), ([0, 1], 2), ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)]
)
class TestSolution:
    def test_missingNumber(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.missingNumber(
                nums,
            )
            == output
        )
