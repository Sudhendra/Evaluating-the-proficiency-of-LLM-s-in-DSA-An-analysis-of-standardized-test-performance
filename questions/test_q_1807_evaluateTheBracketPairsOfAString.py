import pytest
from q_1807_evaluateTheBracketPairsOfAString import Solution


@pytest.mark.parametrize(
    "s, knowledge, output",
    [
        (
            "(name)is(age)yearsold",
            [["name", "bob"], ["age", "two"]],
            "bobistwoyearsold",
        ),
        ("hi(name)", [["a", "b"]], "hi?"),
        ("(a)(a)(a)aaa", [["a", "yes"]], "yesyesyesaaa"),
    ],
)
class TestSolution:
    def test_evaluate(self, s: str, knowledge: List[List[str]], output: str):
        sc = Solution()
        assert (
            sc.evaluate(
                s,
                knowledge,
            )
            == output
        )
