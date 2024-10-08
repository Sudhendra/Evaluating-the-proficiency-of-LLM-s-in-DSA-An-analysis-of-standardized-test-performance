import pytest
from q_0543_diameterOfBinaryTree import Solution


@pytest.mark.parametrize("root, output", [([1, 2, 3, 4, 5], 3), ([1, 2], 1)])
class TestSolution:
    def test_diameterOfBinaryTree(self, root: Optional[TreeNode], output: int):
        sc = Solution()
        assert (
            sc.diameterOfBinaryTree(
                root,
            )
            == output
        )
