import pytest
from q_0330_patchingArray import Solution


@pytest.mark.parametrize(
    "nums, n, output", [([1, 3], 6, 1), ([1, 5, 10], 20, 2), ([1, 2, 2], 5, 0)]
)
class TestSolution:
    def test_minPatches(self, nums: List[int], n: int, output: int):
        sc = Solution()
        assert (
            sc.minPatches(
                nums,
                n,
            )
            == output
        )
