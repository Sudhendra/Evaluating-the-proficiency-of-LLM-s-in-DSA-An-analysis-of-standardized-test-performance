import pytest
from q_1681_minimumIncompatibility import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([1, 2, 1, 4], 2, 4),
        ([6, 3, 8, 1, 3, 1, 2, 2], 4, 6),
        ([5, 3, 3, 6, 3, 3], 3, -1),
    ],
)
class TestSolution:
    def test_minimumIncompatibility(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minimumIncompatibility(
                nums,
                k,
            )
            == output
        )
