import pytest
from q_0722_removeComments import Solution


@pytest.mark.parametrize(
    "source, output",
    [
        (
            [
                "/*Test program */",
                "int main()",
                "{ ",
                "  // variable declaration ",
                "int a, b, c;",
                "/* This is a test",
                "   multiline  ",
                "   comment for ",
                "   testing */",
                "a = b + c;",
                "}",
            ],
            ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"],
        ),
        (["a/*comment", "line", "more_comment*/b"], ["ab"]),
    ],
)
class TestSolution:
    def test_removeComments(self, source: List[str], output: List[str]):
        sc = Solution()
        assert (
            sc.removeComments(
                source,
            )
            == output
        )
