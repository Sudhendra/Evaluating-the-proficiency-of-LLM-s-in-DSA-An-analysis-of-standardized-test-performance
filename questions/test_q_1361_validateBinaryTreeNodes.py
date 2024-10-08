import pytest
from q_1361_validateBinaryTreeNodes import Solution


@pytest.mark.parametrize(
    "n, leftChild, rightChild, output",
    [
        (4, [1, -1, 3, -1], [2, -1, -1, -1], True),
        (4, [1, -1, 3, -1], [2, 3, -1, -1], False),
        (2, [1, 0], [-1, -1], False),
    ],
)
class TestSolution:
    def test_validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int], output: bool
    ):
        sc = Solution()
        assert (
            sc.validateBinaryTreeNodes(
                n,
                leftChild,
                rightChild,
            )
            == output
        )
