import pytest
from q_0129_sumRootToLeafNumbers import Solution


@pytest.mark.parametrize("root, output", [([1, 2, 3], 25), ([4, 9, 0, 5, 1], 1026)])
class TestSolution:
    def test_sumNumbers(self, root: Optional[TreeNode], output: int):
        sc = Solution()
        assert (
            sc.sumNumbers(
                root,
            )
            == output
        )
