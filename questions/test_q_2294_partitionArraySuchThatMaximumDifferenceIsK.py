import pytest
from q_2294_partitionArraySuchThatMaximumDifferenceIsK import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([3, 6, 1, 2, 5], 2, 2), ([1, 2, 3], 1, 2), ([2, 2, 4, 5], 0, 3)],
)
class TestSolution:
    def test_partitionArray(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.partitionArray(
                nums,
                k,
            )
            == output
        )
