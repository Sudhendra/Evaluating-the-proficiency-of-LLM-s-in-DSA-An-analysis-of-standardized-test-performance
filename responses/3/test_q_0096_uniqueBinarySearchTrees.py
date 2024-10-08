import pytest
from q_0096_uniqueBinarySearchTrees import Solution


@pytest.mark.parametrize("n, output", [(3, 5), (1, 1)])
class TestSolution:
    def test_numTrees(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.numTrees(
                n,
            )
            == output
        )
