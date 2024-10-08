import pytest
from q_1678_goalParserInterpretation import Solution


@pytest.mark.parametrize(
    "command, output",
    [("G()(al)", "Goal"), ("G()()()()(al)", "Gooooal"), ("(al)G(al)()()G", "alGalooG")],
)
class TestSolution:
    def test_interpret(self, command: str, output: str):
        sc = Solution()
        assert (
            sc.interpret(
                command,
            )
            == output
        )
