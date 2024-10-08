import pytest
from q_1592_rearrangeSpacesBetweenWords import Solution


@pytest.mark.parametrize(
    "text, output",
    [
        ("  this   is  a sentence ", "this   is   a   sentence"),
        (" practice   makes   perfect", "practice   makes   perfect "),
    ],
)
class TestSolution:
    def test_reorderSpaces(self, text: str, output: str):
        sc = Solution()
        assert (
            sc.reorderSpaces(
                text,
            )
            == output
        )
