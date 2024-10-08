import pytest
from q_1022_sumOfRootToLeafBinaryNumbers import Solution


@pytest.mark.parametrize("root, output", [([1, 0, 1, 0, 1, 0, 1], 22), ([0], 0)])
class TestSolution:
    def test_sumRootToLeaf(self, root: Optional[TreeNode], output: int):
        sc = Solution()
        assert (
            sc.sumRootToLeaf(
                root,
            )
            == output
        )
