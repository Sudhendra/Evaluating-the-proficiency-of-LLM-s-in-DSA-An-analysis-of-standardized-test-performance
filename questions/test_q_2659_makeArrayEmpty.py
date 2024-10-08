import pytest
from q_2659_makeArrayEmpty import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 4, -1], 5), ([1, 2, 4, 3], 5), ([1, 2, 3], 3)]
)
class TestSolution:
    def test_countOperationsToEmptyArray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countOperationsToEmptyArray(
                nums,
            )
            == output
        )
