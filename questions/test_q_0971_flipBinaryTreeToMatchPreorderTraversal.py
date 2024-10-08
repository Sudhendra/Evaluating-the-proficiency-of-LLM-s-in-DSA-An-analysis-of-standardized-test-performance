import pytest
from q_0971_flipBinaryTreeToMatchPreorderTraversal import Solution


@pytest.mark.parametrize(
    "root, voyage, output",
    [([1, 2], [2, 1], [-1]), ([1, 2, 3], [1, 3, 2], [1]), ([1, 2, 3], [1, 2, 3], [])],
)
class TestSolution:
    def test_flipMatchVoyage(
        self, root: Optional[TreeNode], voyage: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.flipMatchVoyage(
                root,
                voyage,
            )
            == output
        )
