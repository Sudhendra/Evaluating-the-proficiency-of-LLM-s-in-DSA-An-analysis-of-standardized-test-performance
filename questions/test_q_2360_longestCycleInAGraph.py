import pytest
from q_2360_longestCycleInAGraph import Solution


@pytest.mark.parametrize("edges, output", [([3, 3, 4, 2, 3], 3), ([2, -1, 3, 1], -1)])
class TestSolution:
    def test_longestCycle(self, edges: List[int], output: int):
        sc = Solution()
        assert (
            sc.longestCycle(
                edges,
            )
            == output
        )
