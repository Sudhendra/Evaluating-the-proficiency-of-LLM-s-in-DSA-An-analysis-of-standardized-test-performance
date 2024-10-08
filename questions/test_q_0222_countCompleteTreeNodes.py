import pytest
from q_0222_countCompleteTreeNodes import Solution


@pytest.mark.parametrize("root, output", [([1, 2, 3, 4, 5, 6], 6), ([], 0), ([1], 1)])
class TestSolution:
    def test_countNodes(self, root: Optional[TreeNode], output: int):
        sc = Solution()
        assert (
            sc.countNodes(
                root,
            )
            == output
        )
