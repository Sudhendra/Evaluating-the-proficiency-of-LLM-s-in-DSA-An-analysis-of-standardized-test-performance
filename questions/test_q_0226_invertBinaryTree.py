import pytest
from q_0226_invertBinaryTree import Solution


@pytest.mark.parametrize(
    "root, output",
    [([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]), ([2, 1, 3], [2, 3, 1]), ([], [])],
)
class TestSolution:
    def test_invertTree(self, root: Optional[TreeNode], output: Optional[TreeNode]):
        sc = Solution()
        assert (
            sc.invertTree(
                root,
            )
            == output
        )
