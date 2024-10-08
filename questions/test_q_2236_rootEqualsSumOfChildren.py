import pytest
from q_2236_rootEqualsSumOfChildren import Solution


@pytest.mark.parametrize("root, output", [([10, 4, 6], True), ([5, 3, 1], False)])
class TestSolution:
    def test_checkTree(self, root: Optional[TreeNode], output: bool):
        sc = Solution()
        assert (
            sc.checkTree(
                root,
            )
            == output
        )
