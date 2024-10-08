import pytest
from q_0331_verifyPreorderSerializationOfABinaryTree import Solution


@pytest.mark.parametrize(
    "preorder, output",
    [("9,3,4,#,#,1,#,#,2,#,6,#,#", True), ("1,#", False), ("9,#,#,1", False)],
)
class TestSolution:
    def test_isValidSerialization(self, preorder: str, output: bool):
        sc = Solution()
        assert (
            sc.isValidSerialization(
                preorder,
            )
            == output
        )
