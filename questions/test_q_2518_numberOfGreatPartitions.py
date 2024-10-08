import pytest
from q_2518_numberOfGreatPartitions import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 2, 3, 4], 4, 6), ([3, 3, 3], 4, 0), ([6, 6], 2, 2)]
)
class TestSolution:
    def test_countPartitions(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.countPartitions(
                nums,
                k,
            )
            == output
        )
