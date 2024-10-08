import pytest
from q_0508_mostFrequentSubtreeSum import Solution


@pytest.mark.parametrize("root, output", [([5, 2, -3], [2, -3, 4]), ([5, 2, -5], [2])])
class TestSolution:
    def test_findFrequentTreeSum(self, root: Optional[TreeNode], output: List[int]):
        sc = Solution()
        assert (
            sc.findFrequentTreeSum(
                root,
            )
            == output
        )
