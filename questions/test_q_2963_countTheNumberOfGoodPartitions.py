import pytest
from q_2963_countTheNumberOfGoodPartitions import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 4], 8), ([1, 1, 1, 1], 1), ([1, 2, 1, 3], 2)]
)
class TestSolution:
    def test_numberOfGoodPartitions(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.numberOfGoodPartitions(
                nums,
            )
            == output
        )
