import pytest
from q_0979_distributeCoinsInBinaryTree import Solution


@pytest.mark.parametrize("root, output", [([3, 0, 0], 2), ([0, 3, 0], 3)])
class TestSolution:
    def test_distributeCoins(self, root: Optional[TreeNode], output: int):
        sc = Solution()
        assert (
            sc.distributeCoins(
                root,
            )
            == output
        )
