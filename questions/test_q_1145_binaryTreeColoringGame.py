import pytest
from q_1145_binaryTreeColoringGame import Solution


@pytest.mark.parametrize(
    "root, n, x, output",
    [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11, 3, True), ([1, 2, 3], 3, 1, False)],
)
class TestSolution:
    def test_btreeGameWinningMove(
        self, root: Optional[TreeNode], n: int, x: int, output: bool
    ):
        sc = Solution()
        assert (
            sc.btreeGameWinningMove(
                root,
                n,
                x,
            )
            == output
        )
