import pytest
from q_1959_minimumTotalSpaceWastedWithKResizingOperations import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([10, 20], 0, 10), ([10, 20, 30], 1, 10), ([10, 20, 15, 30, 20], 2, 15)],
)
class TestSolution:
    def test_minSpaceWastedKResizing(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minSpaceWastedKResizing(
                nums,
                k,
            )
            == output
        )
