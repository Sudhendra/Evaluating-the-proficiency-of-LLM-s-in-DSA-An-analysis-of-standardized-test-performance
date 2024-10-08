import pytest
from q_2440_createComponentsWithSameValue import Solution


@pytest.mark.parametrize(
    "nums, edges, output",
    [([6, 2, 2, 2, 6], [[0, 1], [1, 2], [1, 3], [3, 4]], 2), ([2], [], 0)],
)
class TestSolution:
    def test_componentValue(self, nums: List[int], edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.componentValue(
                nums,
                edges,
            )
            == output
        )
