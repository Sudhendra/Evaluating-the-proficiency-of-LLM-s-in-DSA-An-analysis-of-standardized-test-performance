import pytest
from q_0547_numberOfProvinces import Solution


@pytest.mark.parametrize(
    "isConnected, output",
    [([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2), ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3)],
)
class TestSolution:
    def test_findCircleNum(self, isConnected: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.findCircleNum(
                isConnected,
            )
            == output
        )
