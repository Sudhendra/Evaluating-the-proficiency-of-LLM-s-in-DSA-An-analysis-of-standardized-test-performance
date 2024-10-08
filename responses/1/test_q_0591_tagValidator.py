import pytest
from q_0591_tagValidator import Solution


@pytest.mark.parametrize(
    "code, output",
    [
        ("<DIV>This is the first line <![CDATA[<div>]]></DIV>", True),
        ("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>", True),
        ("<A>  <B> </A>   </B>", False),
    ],
)
class TestSolution:
    def test_isValid(self, code: str, output: bool):
        sc = Solution()
        assert (
            sc.isValid(
                code,
            )
            == output
        )
