import pytest
from q_0889_constructBinaryTreeFromPreorderAndPostorderTraversal import Solution


@pytest.mark.parametrize(
    "preorder, postorder, output",
    [
        ([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1], [1, 2, 3, 4, 5, 6, 7]),
        ([1], [1], [1]),
    ],
)
class TestSolution:
    def test_constructFromPrePost(
        self, preorder: List[int], postorder: List[int], output: Optional[TreeNode]
    ):
        sc = Solution()
        assert (
            sc.constructFromPrePost(
                preorder,
                postorder,
            )
            == output
        )
