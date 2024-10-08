import pytest
from q_2468_splitMessageBasedOnLimit import Solution


@pytest.mark.parametrize(
    "message, limit, output",
    [
        (
            "this is really a very awesome message",
            9,
            [
                "thi<1/14>",
                "s i<2/14>",
                "s r<3/14>",
                "eal<4/14>",
                "ly <5/14>",
                "a v<6/14>",
                "ery<7/14>",
                " aw<8/14>",
                "eso<9/14>",
                "me<10/14>",
                " m<11/14>",
                "es<12/14>",
                "sa<13/14>",
                "ge<14/14>",
            ],
        ),
        ("short message", 15, ["short mess<1/2>", "age<2/2>"]),
    ],
)
class TestSolution:
    def test_splitMessage(self, message: str, limit: int, output: List[str]):
        sc = Solution()
        assert (
            sc.splitMessage(
                message,
                limit,
            )
            == output
        )
