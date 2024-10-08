import pytest
from q_0700_searchInABinarySearchTree import Solution


@pytest.mark.parametrize(
    "root, val, output", [([4, 2, 7, 1, 3], 2, [2, 1, 3]), ([4, 2, 7, 1, 3], 5, [])]
)
class TestSolution:
    def test_searchBST(
        self, root: Optional[TreeNode], val: int, output: Optional[TreeNode]
    ):
        sc = Solution()
        assert (
            sc.searchBST(
                root,
                val,
            )
            == output
        )
